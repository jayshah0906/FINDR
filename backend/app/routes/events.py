"""Event routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from app.database import get_db
from app.models.request_response import EventResponse

router = APIRouter()

# In-memory events storage (can be replaced with database)
EVENTS_STORAGE = [
    {
        "id": 1,
        "name": "Music Festival",
        "zone_id": 1,
        "date": "2026-02-07",
        "start_time": "18:00",
        "end_time": "22:00",
        "expected_impact": "High"
    },
    {
        "id": 2,
        "name": "Business Conference",
        "zone_id": 2,
        "date": "2026-02-07",
        "start_time": "09:00",
        "end_time": "17:00",
        "expected_impact": "Medium"
    },
    {
        "id": 3,
        "name": "Weekend Market",
        "zone_id": 3,
        "date": "2026-02-08",
        "start_time": "10:00",
        "end_time": "16:00",
        "expected_impact": "High"
    }
]


async def get_events_for_zone(
    zone_id: int,
    date: str,
    db: Session
) -> List[EventResponse]:
    """Get events for a specific zone on a given date."""
    events = [
        EventResponse(**event)
        for event in EVENTS_STORAGE
        if event["zone_id"] == zone_id and event["date"] == date
    ]
    return events


@router.get("/events", response_model=List[EventResponse])
async def get_events(
    zone_id: Optional[int] = None,
    date: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get all events, optionally filtered by zone and date."""
    events = EVENTS_STORAGE
    
    if zone_id:
        events = [e for e in events if e["zone_id"] == zone_id]
    
    if date:
        events = [e for e in events if e["date"] == date]
    
    return [EventResponse(**event) for event in events]


@router.get("/events/{event_id}", response_model=EventResponse)
async def get_event(event_id: int, db: Session = Depends(get_db)):
    """Get a specific event by ID."""
    event = next((e for e in EVENTS_STORAGE if e["id"] == event_id), None)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return EventResponse(**event)
