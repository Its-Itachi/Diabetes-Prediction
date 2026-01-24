from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import numpy as np


# Correct absolute imports

from app.schemas import DiabetesInput
from app.auth import verify_token
from app.model_loader import model, scaler

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



# JWT Dependency

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload



# Protected Prediction Endpoint

@router.post("/predict")
def predict(data: DiabetesInput, user=Depends(get_current_user)):
    """
    Predict diabetes outcome.
    Requires a valid JWT token.
    """

    # Convert request data to numpy array
    features = np.array([list(data.dict().values())])

    # IMPORTANT: Apply same scaler used during training
    features_scaled = scaler.transform(features)

    # Model prediction
    prediction = model.predict(features_scaled)[0]

    return {
        "diabetes": int(prediction)
    }
