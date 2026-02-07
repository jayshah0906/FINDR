"""Event routes for MongoDB."""
from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import datetime
import json
import os
from app.models.request_response import EventResponse

router = APIRouter()

# Load events from JSON file
def load_events_from_file():
    """Load events from the ML data folder."""
    events_path = os.path.join(os.path.dirname(__file__), '../../../ml/data/processed/events.json')
    try:
        with open(events_path, 'r') as f:
            events_data = json.load(f)
        
        # Transform to match our API format
        transformed_events = []
        zone_mapping = {
            "BF_001": 1, "BF_002": 2, "BF_003": 3, "BF_004": 4,
            "BF_045": 6, "BF_046": 7, "BF_047": 6, "BF_048": 7,
            "BF_120": 4, "BF_121": 8, "BF_122": 8,
            "BF_200": 9, "BF_201": 9, "BF_202": 10, "BF_203": 10,
            "BF_005": 1
        }
        
        for idx, event in enumerate(events_data, 1):
            # Get all affected zones
            affected_zones = []
            for zone_code in event.get('nearby_zones', []):
                if zone_code in zone_mapping:
                    zone_id = zone_mapping[zone_code]
                    if zone_id not in affected_zones:
                        affected_zones.append(zone_id)
            
            # Create event entry for each affected zone
            for zone_id in affected_zones:
                transformed_events.append({
                    "id": f"{event['event_id']}_{zone_id}",
                    "name": event['event_name'],
                    "zone_id": zone_id,
                    "date": event['date'],
                    "start_time": event['start_time'],
                    "end_time": "23:00",  # Default end time
                    "expected_impact": event['impact_level'].replace('_', ' ').title(),
                    "event_type": event['event_type'],
                    "venue": event['venue'],
                    "expected_attendance": event['expected_attendance']
                })
        
        return transformed_events
    except Exception as e:
        print(f"Error loading events: {e}")
        return []

# Load events at startup
EVENTS_STORAGE = load_events_from_file()


async def get_events_for_zone(
    zone_id: int,
    date: str
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
    date: Optional[str] = None
):
    """Get all events, optionally filtered by zone and date."""
    events = EVENTS_STORAGE
    
    if zone_id:
        events = [e for e in events if e["zone_id"] == zone_id]
    
    if date:
        events = [e for e in events if e["date"] == date]
    
    return [EventResponse(**event) for event in events]


@router.get("/events/date/{date}")
async def get_events_by_date(date: str):
    """Get all events for a specific date with zone information."""
    events = [e for e in EVENTS_STORAGE if e["date"] == date]
    
    # Group by zone
    zones_with_events = {}
    for event in events:
        zone_id = event["zone_id"]
        if zone_id not in zones_with_events:
            zones_with_events[zone_id] = []
        zones_with_events[zone_id].append(event)
    
    return {
        "date": date,
        "total_events": len(events),
        "zones_affected": list(zones_with_events.keys()),
        "events": events,
        "zones_with_events": zones_with_events
    }


@router.get("/events/{event_id}")
async def get_event(event_id: str):
    """Get a specific event by ID."""
    event = next((e for e in EVENTS_STORAGE if e["id"] == event_id), None)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return EventResponse(**event)
