# requestor/app/main.py

from fastapi import FastAPI, HTTPException
from .models import NotificationRequest
from .sqs_client import send_message_to_queue
import logging
import sys

app = FastAPI()

logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/request")
def notify(req: NotificationRequest):
    try:
        response = send_message_to_queue(req.dict())
        logging.info(f"NotificationRequest payload: {response}")
        logging.info(f"NotificationRequest payload: {req.dict()}")
        return {
            "message_id": response.get("MessageId"),
            "status": "queued"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
