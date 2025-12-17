from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pymongo import MongoClient

# ---------------- APP ----------------
app = FastAPI(title="AI Maintenance Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # demo purpose
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- DB ----------------
MONGO_URI = "mongodb+srv://db09762:Deepak%4029@cluster0.pscd3cb.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["ai_maintenance"]
bookings_collection = db["service_bookings"]

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


# ---------------- ROUTES ----------------
@app.get("/")
def root():
    return {"status": "Backend running", "message": "AI Maintenance Platform API is live"}


# --------- AI HEALTH PREDICTION ---------
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


# --------- SERVICE BOOKING ---------
@app.post("/book-service")
def book_service(data: BookingRequest):
    booking = {
        "vehicle_id": data.vehicle_id,
        "service_center": data.service_center,
        "date": data.date,
        "time_slot": data.time_slot,
        "detected_issue": "Clutch system wear",
        "status": "CONFIRMED"
    }

    bookings_collection.insert_one(booking)

    return {"message": "Service booking confirmed"}


# --------- MANUFACTURING INSIGHTS ---------
@app.post("/manufacturing-insights")
def manufacturing_insights(data: ManufacturingRequest):
    count = bookings_collection.count_documents({
        "detected_issue": data.issue_name
    })

    if count >= 3:
        return {
            "issue": data.issue_name,
            "severity": "Medium",
            "recurrence_count": count,
            "RCA": [
                "Accelerated wear due to frequent clutch usage",
                "Urban stop-and-go driving conditions"
            ],
            "CAPA": [
                "Improve clutch material quality",
                "Update preventive maintenance intervals"
            ]
        }

    return {
        "issue": data.issue_name,
        "severity": "Low",
        "recurrence_count": count,
        "RCA": ["Isolated service incident"],
        "CAPA": ["Monitor future occurrences"]
    }


# --------- ANALYTICS ---------
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
    total = bookings_collection.count_documents({})
    high = bookings_collection.count_documents({"detected_issue": "Clutch system wear"})
    medium = max(0, total - high)
    low = max(0, total - high - medium)

    return {
        "low": low,
        "medium": medium,
        "high": high
    }


# --------- RENDER SAFE START ---------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
