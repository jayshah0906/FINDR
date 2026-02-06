"""Seed database with default zones."""
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app.models.zone_model import Zone
from app.config import settings


def seed_zones():
    """Seed zones into database."""
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        # Check if zones already exist
        existing_zones = db.query(Zone).count()
        if existing_zones > 0:
            print("Zones already seeded.")
            return
        
        # Add default zones
        for zone_data in settings.DEFAULT_ZONES:
            zone = Zone(
                id=zone_data["id"],
                name=zone_data["name"],
                latitude=zone_data["lat"],
                longitude=zone_data["lng"],
                description=f"Parking zone: {zone_data['name']}"
            )
            db.add(zone)
        
        db.commit()
        print(f"Seeded {len(settings.DEFAULT_ZONES)} zones successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error seeding zones: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_zones()
