"""Feature building service for ML predictions."""
from typing import Dict
from app.utils.time_utils import get_time_features, get_time_of_day_label
from app.utils.traffic_utils import get_traffic_level, get_traffic_impact
from app.utils.event_utils import check_events_nearby
from app.models.request_response import EventResponse


def build_features(
    zone_id: int,
    date_str: str,
    hour: int,
    day_of_week: int,
    events: list = None
) -> Dict:
    """Build feature vector for prediction.
    
    Args:
        zone_id: Zone identifier
        date_str: Date in YYYY-MM-DD format
        hour: Hour of day
        day_of_week: Day of week
        events: List of events
    
    Returns:
        Dictionary of features
    """
    # Time features
    time_features = get_time_features(date_str, hour, day_of_week)
    
    # Traffic features
    traffic_level = get_traffic_level(zone_id, hour, day_of_week)
    traffic_impact = get_traffic_impact(traffic_level)
    
    # Event features
    event_info = {"events_nearby": 0, "event_names": [], "event_impact": 0.0}
    if events:
        event_info = check_events_nearby(zone_id, date_str, hour, events)
    
    # Zone-specific features
    zone_features = {
        "zone_id": zone_id,
        "is_business_district": zone_id in [1, 2],
        "is_shopping_area": zone_id == 3,
        "is_residential": zone_id == 4,
        "is_educational": zone_id == 5,
    }
    
    # Combine all features
    features = {
        **time_features,
        **zone_features,
        "traffic_level": traffic_level,
        "traffic_impact": traffic_impact,
        "event_impact": event_info["event_impact"],
        "events_count": event_info["events_nearby"],
    }
    
    return features


def get_feature_vector(features: Dict) -> list:
    """Convert features dictionary to numerical vector for ML model.
    
    Args:
        features: Dictionary of features
    
    Returns:
        List of numerical values
    """
    return [
        features["hour"],
        features["day_of_week"],
        float(features["is_weekend"]),
        float(features["is_weekday"]),
        float(features["is_morning"]),
        float(features["is_afternoon"]),
        float(features["is_evening"]),
        float(features["is_night"]),
        float(features["is_rush_hour"]),
        features["month"],
        features["day_of_month"],
        float(features["is_business_district"]),
        float(features["is_shopping_area"]),
        float(features["is_residential"]),
        float(features["is_educational"]),
        features["traffic_impact"],
        features["event_impact"],
        features["events_count"],
    ]
