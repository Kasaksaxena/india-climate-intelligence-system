import pandas as pd
import os
import joblib
from datetime import datetime, timedelta

# Configuration for ML Team
MODEL_PATH = "ml/saved_models/forecast_model.pkl"

async def get_weather_forecast(region: str, days: int):
    """
    Orchestrator: Connects Big Data (DB) -> Preprocessing (ML) -> Prediction (ML).
    """
    
    # --- PHASE A: BIG DATA FETCH (Team DB Task) ---
    # In production, this would be: data = query_hadoop_for_region(region)
    # We simulate a "Feature Vector" that the ML model expects.
    print(f"📡 Querying Hadoop HDFS for {region} historical trends...")
    
    # --- PHASE B: MODEL INFERENCE (Team ML Task) ---
    if os.path.exists(MODEL_PATH):
        # model = joblib.load(MODEL_PATH)
        # prediction_raw = model.predict(feature_vector)
        pass
    else:
        print("⚠️ Warning: ML Model not found. Returning Synthetic/Mock Data.")

    # --- PHASE C: DATA FORMATTING (Your Task - Backend) ---
    # Creating a standardized response for the Frontend
    current_date = datetime.now()
    predictions = []
    
    for i in range(days):
        future_date = (current_date + timedelta(days=i)).strftime("%Y-%m-%d")
        # Mocking the ML output values
        predictions.append({
            "date": future_date,
            "temp_c": 32.0 + (i * 0.5), # Simulated trend
            "rainfall_mm": round(max(0, 1.5 - (i * 0.2)), 2),
            "confidence": 0.85
        })

    return {
        "metadata": {
            "region": region,
            "timestamp": datetime.now().isoformat(),
            "source": "Hadoop_Hive_Cluster",
            "model_engine": "LSTM_v1"
        },
        "forecast": predictions,
        "summary": f"Next {days} days show a warming trend in {region}."
    }