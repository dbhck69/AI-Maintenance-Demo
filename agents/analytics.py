from db.mongodb import bookings_collection

def get_risk_distribution():
    """
    Aggregates service data to show risk distribution
    """

    total = bookings_collection.count_documents({})
    high = bookings_collection.count_documents({"detected_issue": "Clutch system wear"})
    medium = max(0, total - high)
    low = max(0, total - high - medium)

    return {
        "low": low,
        "medium": medium,
        "high": high
    }


def get_feature_statistics():
    """
    Simulated feature importance derived from domain understanding
    """

    return {
        "Mileage": 0.45,
        "Service Gap": 0.30,
        "Usage Pattern": 0.15,
        "Temperature": 0.10
    }