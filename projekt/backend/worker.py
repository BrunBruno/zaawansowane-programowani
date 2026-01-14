import pika
import json
from ultralytics import YOLO
from PIL import Image
import numpy as np
import requests
import io
from job_store import finish_job
import os

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")

model = YOLO("yolov8n.pt")

def count_people(image_np: np.ndarray) -> tuple[int, list]:
    results = model(image_np)
    count = 0
    boxes_list = []

    for r in results:
        if r.boxes is not None:
            cls_array = r.boxes.cls.cpu().numpy()
            xyxy_array = r.boxes.xyxy.cpu().numpy()
            for cls, xyxy in zip(cls_array, xyxy_array):
                if cls == 0:
                    count += 1
                    boxes_list.append(xyxy.tolist())

    return count, boxes_list


def callback(ch, method, properties, body):
    job = json.loads(body)
    job_id = job["job_id"]
    image = 0

    try:
        if job["source_type"] == "upload":
            image_bytes = bytes.fromhex(job["payload"])
            image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

        elif job["source_type"] == "local":
            image = Image.open(job["payload"]).convert("RGB")

        elif job["source_type"] == "url":
            r = requests.get(job["payload"], timeout=10)
            image = Image.open(io.BytesIO(r.content)).convert("RGB")


        elif job["source_type"] == "url":
            r = requests.get(job["payload"], timeout=10)
            image = Image.open(io.BytesIO(r.content)).convert("RGB")

        image_np = np.array(image)
        count, boxes = count_people(image_np)
        finish_job(job_id, {"count": count, "boxes": boxes})

    except Exception:
        finish_job(job_id, -1)

    ch.basic_ack(delivery_tag=method.delivery_tag)

import time

def connect_rabbitmq():
    while True:
        try:
            print(f"Connecting to RabbitMQ at {RABBITMQ_HOST}...")
            return pika.BlockingConnection(
                pika.ConnectionParameters(
                    host=RABBITMQ_HOST,
                    heartbeat=600,
                    blocked_connection_timeout=300,
                )
            )
        except pika.exceptions.AMQPConnectionError:
            print("RabbitMQ not ready, retrying in 5 seconds...")
            time.sleep(5)

connection = connect_rabbitmq()


channel = connection.channel()
channel.queue_declare(queue="image_jobs", durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue="image_jobs", on_message_callback=callback)

print("Worker started...")
channel.start_consuming()
