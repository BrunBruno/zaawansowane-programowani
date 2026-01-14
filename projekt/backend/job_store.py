import redis
import json
from typing import Union, List, Dict
import os

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)


def create_job(job_id: str):
    r.set(job_id, json.dumps({"status": "PENDING", "result": None}))

def finish_job(job_id: str, result: Dict[str, Union[int, List[List[float]]]]):
    job = r.get(job_id)
    if not job:
        print(f"Warning: job {job_id} not found")
        return
    job_data = json.loads(job)
    job_data["status"] = "DONE"
    job_data["result"] = result
    r.set(job_id, json.dumps(job_data))

def get_job(job_id: str):
    job = r.get(job_id)
    if not job:
        return None
    return json.loads(job)