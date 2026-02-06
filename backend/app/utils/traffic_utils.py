"""Traffic-related utility functions."""
from typing import Dict
from app.utils.time_utils import get_time_features


def get_traffic_level(zone_id: int, hour: int, day_of_week: int) -> str:
    """Estimate traffic level based on time patterns.
    
    Args:
        zone_id: Zone identifier
        hour: Hour of day
        day_of_week: Day of week
    
    Returns:
        Traffic level: "low", "moderate", "high"
    """
    time_features = get_time_features("2026-02-07", hour, day_of_week)
    
    # Business districts have high traffic during work hours
    if zone_id in [1, 2]:  # Downtown, Business District
        if time_features["is_rush_hour"] and time_features["is_weekday"]:
            return "high"
        elif time_features["is_weekday"]:
            return "moderate"
        else:
            return "low"
    
    # Shopping areas have high traffic on weekends
    elif zone_id == 3:  # Shopping Mall
        if time_features["is_weekend"] and 10 <= hour < 20:
            return "high"
        elif 12 <= hour < 18:
            return "moderate"
        else:
            return "low"
    
    # Residential areas have moderate traffic during rush hours
    elif zone_id == 4:  # Residential Area
        if time_features["is_rush_hour"]:
            return "moderate"
        else:
            return "low"
    
    # University areas have high traffic during class hours
    elif zone_id == 5:  # University Campus
        if time_features["is_weekday"] and 8 <= hour < 18:
            return "high"
        elif time_features["is_weekday"]:
            return "moderate"
        else:
            return "low"
    
    return "moderate"


def get_traffic_impact(traffic_level: str) -> float:
    """Convert traffic level to impact factor (0-1)."""
    traffic_impact = {
        "low": 0.1,
        "moderate": 0.3,
        "high": 0.5
    }
    return traffic_impact.get(traffic_level, 0.3)
