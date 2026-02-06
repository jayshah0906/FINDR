"""Confidence scoring service for predictions."""
from typing import Dict
from app.utils.time_utils import get_time_features


def calculate_confidence(
    features: Dict,
    historical_data_available: bool = True,
    model_accuracy: float = 0.85
) -> float:
    """Calculate confidence score for prediction.
    
    Args:
        features: Feature dictionary
        historical_data_available: Whether historical data exists
        model_accuracy: Base model accuracy
    
    Returns:
        Confidence score between 0 and 1
    """
    confidence = model_accuracy
    
    # Reduce confidence if no historical data
    if not historical_data_available:
        confidence *= 0.7
    
    # Reduce confidence for unusual times (late night, early morning)
    if features["is_night"]:
        confidence *= 0.9
    
    # Increase confidence for common patterns (rush hours, weekdays)
    if features["is_rush_hour"] and features["is_weekday"]:
        confidence *= 1.05
        confidence = min(confidence, 1.0)
    
    # Reduce confidence if multiple events nearby (unpredictable)
    if features.get("events_count", 0) > 2:
        confidence *= 0.85
    
    return round(confidence, 2)
