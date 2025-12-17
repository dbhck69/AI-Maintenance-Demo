from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

from agents.prediction import predict_failure_risk
from agents.booking import create_service_booking
from agents.manufacturing import generate_manufacturing_insights
from agents.analytics import get_risk_distribution, get_feature_statistics

app = FastAPI(
    title="Autonomous AI Maintenance Platform",
    description="Production-grade backend for predictive maintenance and service optimization",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For demo only (production will be restricted)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VehicleData(BaseModel):
    mileage: int
    last_service_km: int

class BookingData(BaseModel):
    vehicle_id: str
    service_center: str
    date: str
    time_slot: str

class ManufacturingRequest(BaseModel):
    issue_name: str

@app.get("/")
def root():
    return {
        "status": "Backend running",
        "message": "AI Maintenance Platform API is live"
    }

@app.post("/predict-risk")
def predict_risk(data: dict):
    result = predict_failure_risk(data.dict())
    return result

@app.post("/book-service")
def book_service(data: BookingData):
    result = create_service_booking(data.dict())
    return result

@app.post("/manufacturing-insights")
def manufacturing_insights(data: ManufacturingRequest):
    result = generate_manufacturing_insights(data.issue_name)
    return result

@app.get("/analytics/risk-distribution")
def analytics_risk_distribution():
    return get_risk_distribution()


@app.get("/analytics/feature-stats")
def analytics_feature_stats():
    return get_feature_statistics()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
