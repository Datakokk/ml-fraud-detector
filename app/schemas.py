from pydantic import BaseModel, Field
from datetime import datetime

class TransactionRequest(BaseModel):
    transaction_id: str
    tx_hash: str
    amount: float
    origin_address: str
    destination_address: str
    date: datetime  # or str if you prefer to handle it as text

class PredictionResponse(BaseModel):
    is_fraud: bool = Field(..., description="Is the transaction fraudulent?")
    risk_score: float = Field(..., ge=0.0, le=1.0, description="Fraud risk score (0–1)")
