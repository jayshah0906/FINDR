"""Common request/response models."""
from typing import Optional
from pydantic import BaseModel


class ZoneResponse(BaseModel):
    """Zone response model."""
    
    id: int
    name: str
    lat: float
    lng: float
    description: Optional[str] = None


class EventResponse(BaseModel):
    """Event response model."""
    
    id: str
    name: str
    zone_id: int
    date: str
    start_time: str
    end_time: str
    expected_impact: str  # "High", "Medium", "Low", "Very High"
    event_type: Optional[str] = None
    venue: Optional[str] = None
    expected_attendance: Optional[int] = None


class ErrorResponse(BaseModel):
    """Error response model."""
    
    error: str
    detail: Optional[str] = None
