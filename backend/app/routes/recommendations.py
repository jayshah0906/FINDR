"""Recommendation routes for alternative parking zones - MongoDB version."""
from fastapi import APIRouter, Query
from typing import List
from pydantic import BaseModel
from app.services.recommendation_service import recommendation_service
from app.routes.events import get_events_for_zone

router = APIRouter()


class RecommendationResponse(BaseModel):
    """Response model for zone recommendation."""
    zone_id: int
    zone_name: str
    availability_level: str
    occupancy: float
    confidence: float
    distance_km: float
    distance_display: str
    recommendation_score: float
    reason: str
    improvement: int


@router.get("/recommendations", response_model=List[RecommendationResponse])
async def get_alternative_zones(
    zone_id: int = Query(..., description="Current zone ID"),
    date: str = Query(..., description="Date in YYYY-MM-DD format"),
    hour: int = Query(..., ge=0, le=23, description="Hour of day (0-23)"),
    day_of_week: int = Query(..., ge=0, le=6, description="Day of week (0=Monday, 6=Sunday)"),
    availability_level: str = Query(..., description="Current zone availability level (High/Medium/Low)"),
    max_recommendations: int = Query(3, ge=1, le=5, description="Maximum number of recommendations"),
    max_distance_km: float = Query(3.0, ge=0.5, le=10.0, description="Maximum distance in kilometers")
):
    """
    Get alternative zone recommendations based on ML predictions.
    
    This endpoint uses the ML model to:
    1. Predict availability for all nearby zones
    2. Calculate distances from the current zone
    3. Score and rank alternatives based on availability improvement and proximity
    4. Return top recommendations with reasoning
    
    Only returns recommendations when current zone has Low or Medium availability.
    """
    # Get events that might affect zones
    events = await get_events_for_zone(zone_id, date)
    
    # Get ML-powered recommendations
    recommendations = recommendation_service.get_alternative_zones(
        current_zone_id=zone_id,
        date_str=date,
        hour=hour,
        day_of_week=day_of_week,
        current_availability_level=availability_level,
        events=events,
        max_recommendations=max_recommendations,
        max_distance_km=max_distance_km
    )
    
    return recommendations
