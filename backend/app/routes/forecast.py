from fastapi import APIRouter, HTTPException
from app.services.forecast_service import get_weather_forecast

router = APIRouter()

@router.get("/forecast/{region}")
async def fetch_forecast(region: str, days: int = 7):
    try:
        data = await get_weather_forecast(region, days)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))