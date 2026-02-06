"""Prediction service for parking availability."""
import pickle
import os
from typing import Dict, Optional
import numpy as np
from app.config import settings
from app.services.feature_builder import build_features, get_feature_vector
from app.services.confidence_service import calculate_confidence
from app.models.prediction_model import AvailabilityLevel


class PredictionService:
    """Service for making parking availability predictions."""
    
    def __init__(self):
        """Initialize prediction service."""
        self.model = None
        self.load_model()
    
    def load_model(self):
        """Load the trained ML model."""
        model_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
            settings.MODEL_PATH.replace("../", "")
        )
        
        # Create a simple rule-based model if file doesn't exist
        if not os.path.exists(model_path):
            self.model = None
        else:
            try:
                with open(model_path, 'rb') as f:
                    self.model = pickle.load(f)
            except Exception as e:
                print(f"Error loading model: {e}")
                self.model = None
    
    def predict_occupancy(
        self,
        zone_id: int,
        date_str: str,
        hour: int,
        day_of_week: int,
        events: list = None
    ) -> Dict:
        """Predict parking occupancy for given parameters.
        
        Args:
            zone_id: Zone identifier
            date_str: Date in YYYY-MM-DD format
            hour: Hour of day
            day_of_week: Day of week
            events: List of events
        
        Returns:
            Dictionary with prediction results
        """
        # Build features
        features = build_features(zone_id, date_str, hour, day_of_week, events)
        
        # Get feature vector
        feature_vector = get_feature_vector(features)
        
        # Make prediction
        if self.model:
            try:
                occupancy = self.model.predict([feature_vector])[0]
                # Ensure occupancy is between 0 and 100
                occupancy = max(0, min(100, float(occupancy)))
            except Exception as e:
                print(f"Model prediction error: {e}")
                occupancy = self._rule_based_prediction(features)
        else:
            occupancy = self._rule_based_prediction(features)
        
        # Calculate confidence
        confidence = calculate_confidence(features)
        
        # Determine availability level
        availability_level = self._occupancy_to_availability(occupancy)
        
        return {
            "occupancy": round(occupancy, 1),
            "availability_level": availability_level,
            "confidence": confidence,
            "features": features
        }
    
    def _rule_based_prediction(self, features: Dict) -> float:
        """Rule-based prediction when ML model is not available.
        
        Args:
            features: Feature dictionary
        
        Returns:
            Predicted occupancy percentage
        """
        base_occupancy = 50.0
        
        # Zone-specific base occupancy
        if features["is_business_district"]:
            base_occupancy = 70.0
        elif features["is_shopping_area"]:
            base_occupancy = 60.0
        elif features["is_residential"]:
            base_occupancy = 40.0
        elif features["is_educational"]:
            base_occupancy = 65.0
        
        # Time adjustments
        if features["is_rush_hour"]:
            base_occupancy += 20.0
        elif features["is_night"]:
            base_occupancy -= 30.0
        elif features["is_morning"]:
            base_occupancy += 10.0
        
        # Weekend adjustments
        if features["is_weekend"]:
            if features["is_shopping_area"]:
                base_occupancy += 15.0
            elif features["is_business_district"]:
                base_occupancy -= 20.0
        
        # Traffic impact
        base_occupancy += features["traffic_impact"] * 30.0
        
        # Event impact
        base_occupancy += features["event_impact"] * 40.0
        
        # Ensure within bounds
        return max(0.0, min(100.0, base_occupancy))
    
    def _occupancy_to_availability(self, occupancy: float) -> AvailabilityLevel:
        """Convert occupancy percentage to availability level.
        
        Args:
            occupancy: Occupancy percentage (0-100)
        
        Returns:
            Availability level
        """
        if occupancy < 50:
            return "High"
        elif occupancy < 80:
            return "Medium"
        else:
            return "Low"


# Singleton instance
prediction_service = PredictionService()
