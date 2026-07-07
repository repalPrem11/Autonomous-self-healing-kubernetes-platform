from fastapi import FastAPI
from datetime import datetime
import socket

app = FastAPI()

hostname = socket.gethostname()


@app.get("/")
def home():
    return {
        "application": "Self-Healing Platform",
        "service": "Payment Service",
        "version": "2.0",
        "status": "Running",
        "message": "Rolling update successful!"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy",
        "time": str(datetime.now()),
        "hostname": hostname
    }


@app.get("/payment")
def payment():
    return {
        "transaction_id": "TXN-1001",
        "amount": 500,
        "currency": "INR",
        "status": "SUCCESS"
    }
