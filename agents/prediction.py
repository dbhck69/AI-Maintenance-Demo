def predict_failure_risk(vehicle_data: dict):
    """
    Production-style stub for failure prediction logic.
    Can be replaced later with ML model (LSTM, etc.)
    """

    mileage = vehicle_data.get("mileage", 0)
    last_service_km = vehicle_data.get("last_service_km", 0)

    # Simple rule-based logic (pilot-ready)
    if mileage - last_service_km > 5000:
        return {
            "risk_level": "HIGH",
            "issue": "Clutch system wear detected",
            "confidence": 0.92,
            "recommended_action": "Schedule service within 5 days"
        }

    return {
        "risk_level": "LOW",
        "issue": "No critical issues detected",
        "confidence": 0.85,
        "recommended_action": "Continue normal usage"
    }
