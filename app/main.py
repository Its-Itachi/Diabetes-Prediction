from fastapi import FastAPI
from app.predict import router as predict_router
from app.auth import create_access_token

app = FastAPI(title="Diabetes Prediction API")



# Login Endpoint (JWT generation)

@app.post("/login")
def login():
    """
    Dummy login endpoint.
    Replace with real user authentication later.
    """
    access_token = create_access_token({"sub": "user"})
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }



# Include Prediction Router

app.include_router(predict_router)
