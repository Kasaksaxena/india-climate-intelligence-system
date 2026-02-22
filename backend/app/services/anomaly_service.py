import numpy as np

async def detect_climate_anomaly(region: str):
    """
    Logic to check if current weather deviates significantly from historical norms.
    """
    
    # Mock Logic for the team: 
    # In reality, you'd pull the last 30 days of data and compare it to a 10-year mean.
    is_anomaly = True 
    anomaly_score = 0.89  # 0 to 1 scale
    
    return {
        "region": region,
        "is_anomaly": is_anomaly,
        "anomaly_score": anomaly_score,
        "detected_in": "Surface Temperature",
        "description": f"Significant deviation detected in {region}. Temperature is 4.2°C above seasonal average."
    }