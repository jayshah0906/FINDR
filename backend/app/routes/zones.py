"""Zone routes for MongoDB."""
from fastapi import APIRouter, HTTPException
from typing import List
from app.database import zones_collection
from app.models.request_response import ZoneResponse
from app.config import settings

router = APIRouter()


@router.get("/zones", response_model=List[ZoneResponse])
async def get_zones():
    """Get all available parking zones."""
    zones = await zones_collection.find().to_list(length=100)
    if not zones:
        # Return default zones if database is empty
        return settings.DEFAULT_ZONES
    
    # Convert MongoDB documents to response format
    return [{
        "id": zone["id"],
        "name": zone["name"],
        "lat": zone["latitude"],
        "lng": zone["longitude"],
        "description": zone.get("description")
    } for zone in zones]


@router.get("/zones/{zone_id}", response_model=ZoneResponse)
async def get_zone(zone_id: int):
    """Get a specific zone by ID."""
    zone = await zones_collection.find_one({"id": zone_id})
    if not zone:
        # Check default zones
        default_zone = next((z for z in settings.DEFAULT_ZONES if z["id"] == zone_id), None)
        if default_zone:
            return default_zone
        raise HTTPException(status_code=404, detail="Zone not found")
    
    return {
        "id": zone["id"],
        "name": zone["name"],
        "lat": zone["latitude"],
        "lng": zone["longitude"],
        "description": zone.get("description")
    }
