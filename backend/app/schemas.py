from pydantic import BaseModel
from typing import List, Optional

# For the ML Team: What a prediction looks like
class ClimatePrediction(BaseModel):
    date: str
    temp_c: float
    rainfall_mm: float
    confidence_interval: List[float]

# For the DB Team: What the response from Hadoop looks like
class ClimateResponse(BaseModel):
    region: str
    state: str
    severity_score: float
    risk_level: str
    predictions: List[ClimatePrediction]
    anomalies_detected: bool