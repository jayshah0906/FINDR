"""Event-related utility functions."""
from datetime import datetime
from typing import List, Dict
from app.models.request_response import EventResponse


def check_events_nearby(
    zone_id: int,
    date_str: str,
    hour: int,
    events: List[EventResponse]
) -> Dict:
    """Check for events happening near the zone at the given time.
    
    Args:
        zone_id: Zone identifier
        date_str: Date in YYYY-MM-DD format
        hour: Hour of day
        events: List of events
    
    Returns:
        Dictionary with event information
    """
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    events_nearby = []
    max_impact = 0
    
    for event in events:
        if event.zone_id == zone_id and event.date == date_str:
            event_start = int(event.start_time.split(":")[0])
            event_end = int(event.end_time.split(":")[0])
            
            # Check if current hour is within event time range
            if event_start <= hour <= event_end:
                events_nearby.append(event.name)
                
                # Determine impact level
                impact_map = {"High": 0.5, "Medium": 0.3, "Low": 0.1}
                impact = impact_map.get(event.expected_impact, 0.1)
                max_impact = max(max_impact, impact)
    
    return {
        "events_nearby": len(events_nearby),
        "event_names": events_nearby,
        "event_impact": max_impact
    }
