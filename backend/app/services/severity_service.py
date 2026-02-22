import random

async def calculate_climate_severity(region: str):
    """
    Core Logic for Feature 1 (Growth), Feature 2 (Temp Change), 
    and Feature 3 (Risk Labeling).
    """
    # Feature 2 Logic: Temperature Volatility (Max - Min)
    # In production, these values will come from your Hadoop/Hive queries
    max_t = 44.5
    min_t = 22.0
    temp_range = round(max_t - min_t, 2)
    
    # Feature 1: Growth Indicator (Rate of change over time)
    # Simulated calculation: (Current Avg - Historical Avg) / Time
    growth_rate = "+0.45°C / decade"
    
    # ML Input: This score will eventually be fetched from the ML team's model
    # Mocking a score based on the region for now
    score = 72.5  
    
    # Feature 3: Climate Risk Label System (4-Tier)
    if score >= 80:
        label, color = "CRITICAL", "Red"
    elif score >= 50:
        label, color = "HIGH RISK", "Orange"
    elif score >= 25:
        label, color = "MODERATE", "Yellow"
    else:
        label, color = "STABLE", "Green"

    return {
        "region": region,
        "analytics": {
            "climate_growth_indicator": growth_rate,
            "temp_volatility_range": f"{temp_range}°C",
            "max_temp_recorded": f"{max_t}°C",
            "min_temp_recorded": f"{min_t}°C"
        },
        "severity": {
            "score": score,
            "label": label,
            "color": color
        }
    }

async def get_regional_rankings(metric: str):
    """
    Feature 2: Country/Region Ranking Leaderboard logic.
    Provides data for the Frontend to display top 'at-risk' or 'high-change' regions.
    """
    # This data will eventually come from a Hive 'ORDER BY' query executed by the DB Team
    rankings_data = [
        {"region": "Rajasthan", "value": 22.5, "unit": "°C Range", "rank": 1},
        {"region": "Punjab", "value": 19.8, "unit": "°C Range", "rank": 2},
        {"region": "Maharashtra", "value": 15.4, "unit": "°C Range", "rank": 3},
        {"region": "Tamil Nadu", "value": 11.2, "unit": "°C Range", "rank": 4},
        {"region": "Kerala", "value": 8.2, "unit": "°C Range", "rank": 5}
    ]
    
    # Logic to return rankings based on the requested metric
    if metric == "risk_score":
        # Just a mock shuffle to show the logic works
        return sorted(rankings_data, key=lambda x: x['value'], reverse=True)
        
    return rankings_data