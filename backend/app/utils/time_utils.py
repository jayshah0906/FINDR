"""Time-related utility functions."""
from datetime import datetime, timedelta
from typing import Tuple


def get_time_features(date_str: str, hour: int, day_of_week: int) -> dict:
    """Extract time-based features for prediction.
    
    Args:
        date_str: Date in YYYY-MM-DD format
        hour: Hour of day (0-23)
        day_of_week: Day of week (0=Monday, 6=Sunday)
    
    Returns:
        Dictionary of time features
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    
    features = {
        "hour": hour,
        "day_of_week": day_of_week,
        "is_weekend": day_of_week >= 5,
        "is_weekday": day_of_week < 5,
        "is_morning": 6 <= hour < 12,
        "is_afternoon": 12 <= hour < 18,
        "is_evening": 18 <= hour < 22,
        "is_night": hour >= 22 or hour < 6,
        "is_rush_hour": (7 <= hour < 9) or (17 <= hour < 19),
        "month": date_obj.month,
        "day_of_month": date_obj.day,
        "is_holiday": False,  # Can be enhanced with holiday calendar
    }
    
    return features


def get_time_of_day_label(hour: int) -> str:
    """Get time of day label."""
    if 6 <= hour < 12:
        return "morning"
    elif 12 <= hour < 18:
        return "afternoon"
    elif 18 <= hour < 22:
        return "evening"
    else:
        return "night"


def parse_datetime(date_str: str, hour: int) -> datetime:
    """Parse date and hour into datetime object."""
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    return date_obj.replace(hour=hour, minute=0, second=0, microsecond=0)
