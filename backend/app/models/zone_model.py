"""Zone model for MongoDB."""
from typing import Optional
from pydantic import BaseModel, Field
from bson import ObjectId


class PyObjectId(ObjectId):
    """Custom ObjectId type for Pydantic."""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Zone(BaseModel):
    """Zone model for MongoDB."""
    mongo_id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    id: int  # Keep integer ID for compatibility with frontend
    name: str
    latitude: float
    longitude: float
    description: Optional[str] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Downtown Pike St",
                "latitude": 47.6105,
                "longitude": -122.3380,
                "description": "Downtown parking zone"
            }
        }

    def to_dict(self):
        """Convert zone to dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "lat": self.latitude,
            "lng": self.longitude,
            "description": self.description
        }
