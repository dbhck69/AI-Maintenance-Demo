from db.mongodb import bookings_collection

def generate_manufacturing_insights(issue_name: str):
    """
    Generate RCA & CAPA based on recurring service issues
    """

    # Count occurrences of the same issue
    recurrence_count = bookings_collection.count_documents({
        "status": "CONFIRMED",
        "detected_issue": issue_name
    })

    if recurrence_count >= 5:
        severity = "HIGH"
        rca = [
            "Design stress concentration near clutch housing",
            "Material degradation under prolonged heat exposure",
            "Inadequate tolerance for urban stop-and-go usage"
        ]
        capa = [
            "Redesign clutch housing for better heat dissipation",
            "Upgrade friction material grade",
            "Introduce urban-usage stress testing during validation"
        ]

    elif recurrence_count >= 3:
        severity = "MEDIUM"
        rca = [
            "Accelerated wear under high-load usage",
            "Suboptimal material performance in traffic conditions"
        ]
        capa = [
            "Improve supplier quality checks",
            "Revise maintenance interval recommendations"
        ]

    else:
        severity = "LOW"
        rca = ["Isolated service occurrence"]
        capa = ["Monitor trend and collect more data"]

    return {
        "issue": issue_name,
        "recurrence_count": recurrence_count,
        "severity": severity,
        "RCA": rca,
        "CAPA": capa
    }
