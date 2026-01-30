from fastapi import FastAPI
import json
from pathlib import Path

app = FastAPI()

FREE_CLASSES_DATA_PATH = Path(__file__).parent / "data" / "free_classes.json"


@app.get("/", summary="Health Check")
def getRoot():
    return {
        "status": "running",
        "version": "1.0.0",
    }


@app.get("/classes", summary="Get all free classes")
def getClasses():
    with open(FREE_CLASSES_DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
