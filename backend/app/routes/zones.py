"""Zone routes."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.zone_model import Zone
from app.models.request_response import ZoneResponse
from app.config import settings

router = APIRouter()


@router.get("/zones", response_model=List[ZoneResponse])
async def get_zones(db: Session = Depends(get_db)):
    """Get all available parking zones."""
    zones = db.query(Zone).all()
    if not zones:
        # Return default zones if database is empty
        return settings.DEFAULT_ZONES
    return [zone.to_dict() for zone in zones]


@router.get("/zones/{zone_id}", response_model=ZoneResponse)
async def get_zone(zone_id: int, db: Session = Depends(get_db)):
    """Get a specific zone by ID."""
    zone = db.query(Zone).filter(Zone.id == zone_id).first()
    if not zone:
        # Check default zones
        default_zone = next((z for z in settings.DEFAULT_ZONES if z["id"] == zone_id), None)
        if default_zone:
            return default_zone
        raise HTTPException(status_code=404, detail="Zone not found")
    return zone.to_dict()
