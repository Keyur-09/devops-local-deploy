from fastapi import FastAPI
import os
from datetime import datetime

app = FastAPI()

APP_NAME = os.getenv("APP_NAME", "Default App")
APP_ENV = os.getenv("APP_ENV", "prod")
APP_VERSION = os.getenv("APP_VERSION", "0.0")

@app.get("/")
def root():
    return {
        "app_name": APP_NAME,
        "environment": APP_ENV,
        "version": APP_VERSION,
        "time": datetime.now()
    }

@app.get("/health")
def health():
    return {"status": "ok"}
