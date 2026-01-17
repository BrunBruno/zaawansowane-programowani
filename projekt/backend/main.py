from fastapi import FastAPI, UploadFile, File, Query
import uuid
import shutil
import os
from rabbitmq import publish_job
from job_store import create_job, get_job
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/count-people-from-local")
def count_from_local():
    job_id = str(uuid.uuid4())
    create_job(job_id)

    publish_job({
        "job_id": job_id,
        "source_type": "local",
        "payload": "people.jpg"
    })

    return {"job_id": job_id}

@app.get("/count-people-from-url")
def count_from_url(image_url: str = Query(...)):
    job_id = str(uuid.uuid4())
    create_job(job_id)

    publish_job({
        "job_id": job_id,
        "source_type": "url",
        "payload": image_url
    })

    return {"job_id": job_id}

@app.post("/count-people-from-uploaded")
async def count_from_upload(file: UploadFile = File(...)):
    job_id = str(uuid.uuid4())
    create_job(job_id)

    content = await file.read()

    publish_job({
        "job_id": job_id,
        "source_type": "upload",
        "payload": content.hex()
    })

    return {"job_id": job_id}

@app.get("/job-status/{job_id}")
def job_status(job_id: str):
    job = get_job(job_id)
    if not job:
        return {"error": "Job not found"}
    return job
