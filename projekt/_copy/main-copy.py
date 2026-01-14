from fastapi import FastAPI, File, UploadFile, HTTPException, Query
from ultralytics import YOLO
from PIL import Image
import numpy as np
import io
import requests
import os

model = YOLO("../backend/yolov8n.pt")

app = FastAPI()

@app.get("/count-people-from-local")
def count_people_from_local():
    local_image_path = "../backend/people.jpg"

    if not os.path.exists(local_image_path):
        raise HTTPException(status_code=500, detail=f"Local image not found: {local_image_path}")

    image = Image.open(local_image_path).convert("RGB")
    image_np = np.array(image)

    result = count_people_from_image_np(image_np)
    return {"result": result}


@app.get("/count-people-from-url")
def count_people_from_url(image_url: str = Query(...)):
    response = requests.get(image_url, timeout=10)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Could not download image")
    content_type = response.headers.get("content-type", "")
    if not content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="URL does not point to an image")

    image = Image.open(io.BytesIO(response.content)).convert("RGB")
    image_np = np.array(image)

    result = count_people_from_image_np(image_np)
    return {"result": result}


@app.post("/count-people-from-uploaded")
async def upload_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image")

    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image_np = np.array(image)

    result = count_people_from_image_np(image_np)
    return {"result": result}


def count_people_from_image_np(image_np: np.ndarray) -> int:
    results = model(image_np)
    people_count = 0

    for r in results:
        if r.boxes is None:
            continue
        classes = r.boxes.cls.cpu().numpy()
        if classes.ndim == 0:
            classes = [classes]
        people_count += int((classes == 0).sum())

    return people_count
