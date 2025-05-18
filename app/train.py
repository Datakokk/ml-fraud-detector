from fastapi import APIRouter
from app.utils.train_model import train_model_pipeline

router = APIRouter()

@router.post("/train")
def train_model_endpoint():
    try:
        train_model_pipeline()
        return {"status": "success", "message": "Modelo entrenado correctamente."}
    except Exception as e:
        return {"status": "error", "message": str(e)}
