from fastapi import APIRouter, HTTPException
from app.services.anomaly_service import detect_climate_anomaly

router = APIRouter()

@router.get("/anomaly/{region}")
async def get_anomaly_status(region: str):
    try:
        # We call the service logic here
        result = await detect_climate_anomaly(region)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))