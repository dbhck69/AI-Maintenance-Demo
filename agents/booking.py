from datetime import datetime
from db.mongodb import bookings_collection

def create_service_booking(booking_data: dict):
    booking = {
    "vehicle_id": booking_data.get("vehicle_id"),
    "service_center": booking_data.get("service_center"),
    "date": booking_data.get("date"),
    "time_slot": booking_data.get("time_slot"),
    "detected_issue": "Clutch system wear",
    "status": "CONFIRMED"
}


    bookings_collection.insert_one(booking)
    return {
        "message": "Service booking confirmed",
        "booking_status": "CONFIRMED"
    }
