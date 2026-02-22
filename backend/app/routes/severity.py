from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.services.severity_service import calculate_climate_severity, get_regional_rankings

router = APIRouter()

@router.get("/severity/{region}")
async def get_severity_index(region: str):
    try:
        return await calculate_climate_severity(region)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/rankings")
async def get_rankings(metric: str = "temp_change"):
    """
    Feature 2: Country/Region Ranking Leaderboard.
    Metrics can be 'temp_change' or 'risk_score'.
    """
    return await get_regional_rankings(metric)

@router.get("/compare")
async def compare_regions(regions: List[str] = Query(...)):
    """
    Feature 4: Comparison Mode. 
    Accepts multiple regions: /compare?regions=Delhi&regions=Mumbai
    """
    results = []
    for region in regions:
        data = await calculate_climate_severity(region)
        results.append(data)
    return {"comparison": results}