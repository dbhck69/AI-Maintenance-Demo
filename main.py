from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AI Maintenance Platform API")

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- MODELS ----------------
class PredictRequest(BaseModel):
    mileage: int
    last_service_km: int
    usage_pattern: str


class BookingRequest(BaseModel):
    vehicle_id: str
    service_center: str
    date: str
    time_slot: str


class ManufacturingRequest(BaseModel):
    issue_name: str


# ---------------- ROOT ----------------
@app.get("/")
def root():
    return {
        "status": "Backend running",
        "message": "AI Maintenance Platform API is live"
    }


# ---------------- AI HEALTH PREDICTION ----------------
@app.post("/predict-risk")
def predict_risk(data: PredictRequest):
    distance = data.mileage - data.last_service_km

    if distance > 8000:
        return {
            "risk_level": "High",
            "issue": "Clutch system wear",
            "recommendation": "Immediate service booking recommended"
        }

    return {
        "risk_level": "Low",
        "issue": "No critical issues detected",
        "recommendation": "Routine monitoring advised"
    }


# ---------------- SERVICE BOOKING ----------------
@app.post("/book-service")
def book_service(data: BookingRequest):
    return {
        "message": "Service booking confirmed",
        "vehicle_id": data.vehicle_id,
        "service_center": data.service_center,
        "status": "CONFIRMED"
    }


# ---------------- MANUFACTURING INSIGHTS ----------------
@app.post("/manufacturing-insights")
def manufacturing_insights(data: ManufacturingRequest):
    return {
        "issue": data.issue_name,
        "severity": "Medium",
        "recurrence_count": 3,
        "RCA": [
            "High clutch usage in urban traffic",
            "Increased stop-and-go driving patterns"
        ],
        "CAPA": [
            "Improve clutch material durability",
            "Adjust preventive maintenance intervals"
        ]
    }


# ---------------- ANALYTICS ----------------
@app.get("/analytics/feature-stats")
def feature_stats():
    return {
        "Mileage": 0.45,
        "Service Gap": 0.30,
        "Usage Pattern": 0.15,
        "Temperature": 0.10
    }


@app.get("/analytics/risk-distribution")
def risk_distribution():
    return {
        "low": 5,
        "medium": 3,
        "high": 2
    }


# ---------------- START ----------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
