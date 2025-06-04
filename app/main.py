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
    # Lista de hashes fraudulentos conocidos
    KNOWN_FRAUD_HASHES = {
        "0xb5c8bd9430b6cc87a0e2fe110ece6bf527fa4f170a4bc8cd032f768fc5219838",
        "0x9999999999999999999999999999999999999999999999999999999999999999",
    }

    # Si el hash está en la lista negra, devolver directamente resultado fraudulento
    if transaction.tx_hash.lower() in KNOWN_FRAUD_HASHES:
        return PredictionResponse(
            is_fraud=True,
            risk_score=0.99
        )

    # Continuar con predicción del modelo
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
