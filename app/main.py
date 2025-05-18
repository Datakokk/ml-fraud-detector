from fastapi import FastAPI, HTTPException
from app.schemas import TransactionRequest, PredictionResponse
from app.utils.train_model import train_model_pipeline
from app.train import router as train_router
from app.status import router as status_router
import joblib
import numpy as np
import os

app = FastAPI(title="ML Fraud Detector")


@app.post("/predict", response_model=PredictionResponse)
def predict(transaction: TransactionRequest):
    try:
        model_path = os.path.abspath("app/model/model.pkl")
        model = joblib.load(model_path)  # Carga el modelo solo cuando se llama al endpoint
        features = np.array([[transaction.amount]])
        prediction = model.predict(features)[0]
        prob = model.predict_proba(features)[0][1]
        return PredictionResponse(is_fraud=bool(prediction), risk_score=float(prob))
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Model file not found. Please train the model first.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Registrar routers
app.include_router(train_router)
app.include_router(status_router)
