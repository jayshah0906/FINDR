"""Configuration settings for the parking prediction API."""
import os
from typing import Optional
from pydantic_settings import BaseSettings


def _project_root():
    """Project root (parent of backend/)."""
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.dirname(backend_dir)


def _ml_paths():
    """Paths to ML model and data (from project root)."""
    root = _project_root()
    return {
        "model": os.path.join(root, "ml", "models", "parking_model.pkl"),
        "data_dir": os.path.join(root, "ml", "data", "processed"),
    }


class Settings(BaseSettings):
    """Application settings."""
    
    # API Settings
    API_TITLE: str = "Parking Availability Prediction API"
    API_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    
    # Database Settings
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./parking_prediction.db"
    )
    
    # Model Settings (legacy; used only if ML not enabled)
    MODEL_PATH: str = os.getenv(
        "MODEL_PATH",
        "../models_store/parking_model.pkl"
    )
    
    # ML integration: paths and zone mapping
    USE_ML_MODEL: bool = os.getenv("USE_ML_MODEL", "true").lower() in ("true", "1", "yes")
    ML_MODEL_PATH: str = os.getenv("ML_MODEL_PATH", _ml_paths()["model"])
    ML_DATA_DIR: str = os.getenv("ML_DATA_DIR", _ml_paths()["data_dir"])
    # Map backend zone_id (1-5) to ML zone_id (e.g. BF_001)
    ML_ZONE_ID_MAP: dict = {
        1: "BF_001",
        2: "BF_002",
        3: "BF_003",
        4: "BF_120",
        5: "BF_200",
    }
    
    # Data Paths
    DATA_DIR: str = os.getenv("DATA_DIR", "../data")
    RAW_DATA_DIR: str = os.path.join(DATA_DIR, "raw")
    PROCESSED_DATA_DIR: str = os.path.join(DATA_DIR, "processed")
    
    # CORS Settings
    CORS_ORIGINS: list = [
        "http://localhost:3000",
        "http://localhost:5173",
        "http://localhost:8080",
    ]
    
    # Prediction Settings
    DEFAULT_CONFIDENCE_THRESHOLD: float = 0.7
    PREDICTION_HORIZON_HOURS: int = 2
    
    # Zone Settings
    DEFAULT_ZONES: list = [
        {"id": 1, "name": "Downtown", "lat": 40.7128, "lng": -74.0060},
        {"id": 2, "name": "Business District", "lat": 40.7589, "lng": -73.9851},
        {"id": 3, "name": "Shopping Mall", "lat": 40.7505, "lng": -73.9934},
        {"id": 4, "name": "Residential Area", "lat": 40.7282, "lng": -73.9942},
        {"id": 5, "name": "University Campus", "lat": 40.8075, "lng": -73.9625},
    ]
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
