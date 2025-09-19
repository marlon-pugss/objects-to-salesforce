from fastapi import FastAPI
from src.io.http.lead import router as lead_router

app = FastAPI(title="Leads to Salesforce API", version="1.0.0")

app.include_router(lead_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Leads to Salesforce API is running"}