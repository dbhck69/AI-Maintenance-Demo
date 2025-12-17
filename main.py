from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="AI Maintenance Demo")

# ---------- CORS ----------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- MODELS ----------
class PredictRequest(BaseModel):
    mileage: int
    last_service_km: int
    usage_pattern: str

class BookingRequest(BaseModel):
    vehicle_id: str
    service_center: str
    date: str
    time_slot: str

# ---------- ROOT ----------
@app.get("/")
def root():
    return {"status": "Backend running"}

# ---------- PREDICTION ----------
@app.post("/predict-risk")
def predict_risk(data: PredictRequest):
    if data.mileage - data.last_service_km > 8000:
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

# ---------- BOOKING (CANNOT FAIL) ----------
@app.post("/book-service")
def book_service(data: BookingRequest):
    return {
        "message": "Service booking confirmed",
        "status": "CONFIRMED",
        "vehicle_id": data.vehicle_id,
        "service_center": data.service_center,
        "date": data.date,
        "time_slot": data.time_slot
    }
