from fastapi import APIRouter
import os
from datetime import datetime

router = APIRouter()

MODEL_PATH = os.path.join("app", "model", "model.pkl")

@router.get("/status")
def get_model_status():
    if not os.path.exists(MODEL_PATH):
        return {
            "status": "missing",
            "message": "Modelo no encontrado.",
            "model_path": MODEL_PATH
        }

    last_modified = os.path.getmtime(MODEL_PATH)
    size_bytes = os.path.getsize(MODEL_PATH)

    return {
        "status": "ready",
        "model_path": MODEL_PATH,
        "last_modified": datetime.fromtimestamp(last_modified).isoformat(),
        "size_kb": round(size_bytes / 1024, 2)
    }
