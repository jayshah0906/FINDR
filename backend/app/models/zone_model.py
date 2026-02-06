"""Zone database model."""
from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Zone(Base):
    """Zone model representing a parking zone in the city."""
    
    __tablename__ = "zones"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    description = Column(String, nullable=True)
    
    def to_dict(self):
        """Convert zone to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "lat": self.latitude,
            "lng": self.longitude,
            "description": self.description
        }
