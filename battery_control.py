from database import collection

async def get_latest_battery_data():
    latest_data = await collection.find_one({}, sort=[("_id", -1)])  # Fetch latest entry
    return latest_data

async def adjust_battery_power():
    data = await get_latest_battery_data()
    if not data:
        return {"status": "No data available"}
    
    risk_probability = data.get("risk_probability", 0)
    
    if risk_probability > 80:  # High risk
        action = "Reduce battery power to 60% and enable max cooling"
    elif risk_probability > 50:  # Medium risk
        action = "Reduce battery power to 80% and enable moderate cooling"
    else:  # Low risk
        action = "Battery operating normally"

    return {
        "risk_probability": risk_probability,
        "status": data.get("status", "Unknown"),
        "action_taken": action
    }
