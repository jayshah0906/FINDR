"""Recommendation service for alternative parking zones."""
import math
import logging
from typing import List, Dict, Optional
from app.services.prediction_service import prediction_service

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def calculate_distance(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    """
    Calculate distance between two coordinates using Haversine formula.
    Returns distance in kilometers.
    """
    R = 6371  # Earth's radius in kilometers
    
    lat1_rad = math.radians(lat1)
    lat2_rad = math.radians(lat2)
    delta_lat = math.radians(lat2 - lat1)
    delta_lng = math.radians(lng2 - lng1)
    
    a = (math.sin(delta_lat / 2) ** 2 +
         math.cos(lat1_rad) * math.cos(lat2_rad) *
         math.sin(delta_lng / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    distance = R * c
    return round(distance, 2)


def get_availability_score(availability_level: str) -> int:
    """Convert availability level to numeric score for comparison."""
    scores = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }
    return scores.get(availability_level, 0)


def generate_recommendation_reason(
    alternative_zone: Dict,
    current_zone: Dict,
    distance: float,
    availability_improvement: int
) -> str:
    """Generate human-readable reason for recommendation."""
    reasons = []
    
    # Distance-based reason
    if distance < 0.5:
        reasons.append("Very close by")
    elif distance < 1.0:
        reasons.append("Short walk away")
    elif distance < 2.0:
        reasons.append("Nearby area")
    
    # Availability improvement
    if availability_improvement == 2:
        reasons.append("much better availability")
    elif availability_improvement == 1:
        reasons.append("better availability")
    
    # Zone type similarity
    alt_features = alternative_zone.get("features", {})
    curr_features = current_zone.get("features", {})
    
    if (alt_features.get("is_business_district") and curr_features.get("is_business_district")):
        reasons.append("similar business area")
    elif (alt_features.get("is_shopping_area") and curr_features.get("is_shopping_area")):
        reasons.append("similar shopping area")
    
    return ", ".join(reasons) if reasons else "alternative option"


class RecommendationService:
    """Service for generating alternative zone recommendations."""
    
    # Zone coordinates (matching frontend ZONES array)
    ZONE_COORDINATES = {
        1: {"lat": 47.6105, "lng": -122.3380, "name": "Downtown Pike St"},
        2: {"lat": 47.6050, "lng": -122.3350, "name": "Downtown 1st Ave"},
        3: {"lat": 47.6080, "lng": -122.3310, "name": "Downtown 3rd Ave"},
        4: {"lat": 47.6240, "lng": -122.3210, "name": "Capitol Hill - Broadway"},
        5: {"lat": 47.6650, "lng": -122.3130, "name": "University District - University Way"},
        6: {"lat": 47.5920, "lng": -122.3330, "name": "Stadium District - Occidental"},
        7: {"lat": 47.5970, "lng": -122.3280, "name": "Stadium District - 1st Ave S"},
        8: {"lat": 47.6180, "lng": -122.3150, "name": "Capitol Hill - Pike St"},
        9: {"lat": 47.6590, "lng": -122.3080, "name": "University District - 45th St"},
        10: {"lat": 47.6505, "lng": -122.3493, "name": "Fremont - Fremont Ave"}
    }
    
    def get_alternative_zones(
        self,
        current_zone_id: int,
        date_str: str,
        hour: int,
        day_of_week: int,
        current_availability_level: str,
        events: list = None,
        max_recommendations: int = 3,
        max_distance_km: float = 3.0
    ) -> List[Dict]:
        """
        Get alternative zone recommendations using ML predictions.
        
        Args:
            current_zone_id: ID of the currently selected zone
            date_str: Date in YYYY-MM-DD format
            hour: Hour of day (0-23)
            day_of_week: Day of week (0=Monday, 6=Sunday)
            current_availability_level: Current zone's availability (High/Medium/Low)
            events: List of events affecting zones
            max_recommendations: Maximum number of recommendations to return
            max_distance_km: Maximum distance in kilometers for recommendations
        
        Returns:
            List of recommended zones with details
        """
        # VALIDATION: Ensure ML model is being used
        if not prediction_service.ml_available:
            logger.error("❌ CRITICAL: ML model is NOT available! Recommendations will use fallback rules.")
            logger.error(f"   ML Model Path: {prediction_service._ml_model_path}")
            logger.error(f"   ML Data Dir: {prediction_service._ml_data_dir}")
            logger.error("   Please ensure ML model is properly loaded!")
        else:
            logger.info(f"✅ ML model is active and will be used for all {len(self.ZONE_COORDINATES)} zones")
            logger.info(f"   Model: {prediction_service._ml_model_path}")
            logger.info(f"   Data: {prediction_service._ml_data_dir}")
        
        if current_zone_id not in self.ZONE_COORDINATES:
            logger.warning(f"Invalid zone_id: {current_zone_id}")
            return []
        
        current_zone = self.ZONE_COORDINATES[current_zone_id]
        current_score = get_availability_score(current_availability_level)
        
        # Only recommend if current availability is Low or Medium
        if current_score >= 3:  # High availability
            logger.info(f"Zone {current_zone_id} has HIGH availability - no recommendations needed")
            return []
        
        logger.info(f"Finding alternatives for Zone {current_zone_id} ({current_zone['name']}) with {current_availability_level} availability")
        
        recommendations = []
        ml_predictions_count = 0
        fallback_predictions_count = 0
        
        # Get predictions for all other zones
        for zone_id, zone_info in self.ZONE_COORDINATES.items():
            if zone_id == current_zone_id:
                continue
            
            # Calculate distance
            distance = calculate_distance(
                current_zone["lat"], current_zone["lng"],
                zone_info["lat"], zone_info["lng"]
            )
            
            # Skip if too far
            if distance > max_distance_km:
                continue
            
            # Get ML prediction for this zone
            try:
                prediction = prediction_service.predict_occupancy(
                    zone_id=zone_id,
                    date_str=date_str,
                    hour=hour,
                    day_of_week=day_of_week,
                    events=events or []
                )
                
                # VALIDATION: Check if ML was actually used
                if prediction_service.ml_available:
                    ml_predictions_count += 1
                    logger.debug(f"  ✅ Zone {zone_id}: ML prediction = {prediction['occupancy']:.1f}% occupancy")
                else:
                    fallback_predictions_count += 1
                    logger.warning(f"  ⚠️  Zone {zone_id}: Using FALLBACK (not ML)")
                
                availability_level = prediction["availability_level"]
                availability_score = get_availability_score(availability_level)
                
                # Only recommend zones with better availability
                if availability_score <= current_score:
                    continue
                
                # Calculate recommendation score
                # Higher score = better recommendation
                availability_improvement = availability_score - current_score
                distance_penalty = distance / max_distance_km
                
                # Weighted scoring: 70% availability improvement, 30% proximity
                recommendation_score = (availability_improvement * 0.7) - (distance_penalty * 0.3)
                
                # Generate reason
                reason = generate_recommendation_reason(
                    alternative_zone={"features": prediction.get("features", {})},
                    current_zone={"features": {}},
                    distance=distance,
                    availability_improvement=availability_improvement
                )
                
                recommendations.append({
                    "zone_id": zone_id,
                    "zone_name": zone_info["name"],
                    "availability_level": availability_level,
                    "occupancy": prediction["occupancy"],
                    "confidence": prediction["confidence"],
                    "distance_km": distance,
                    "distance_display": f"{distance:.1f} km" if distance >= 1 else f"{int(distance * 1000)} m",
                    "recommendation_score": recommendation_score,
                    "reason": reason,
                    "improvement": availability_improvement
                })
                
            except Exception as e:
                logger.error(f"Error predicting for zone {zone_id}: {e}")
                continue
        
        # Log prediction method summary
        total_predictions = ml_predictions_count + fallback_predictions_count
        if total_predictions > 0:
            ml_percentage = (ml_predictions_count / total_predictions) * 100
            logger.info(f"📊 Prediction Summary: {ml_predictions_count}/{total_predictions} used ML ({ml_percentage:.0f}%)")
            if fallback_predictions_count > 0:
                logger.warning(f"⚠️  {fallback_predictions_count} predictions used FALLBACK instead of ML!")
        
        # Sort by recommendation score (highest first)
        recommendations.sort(key=lambda x: x["recommendation_score"], reverse=True)
        
        logger.info(f"Found {len(recommendations)} better alternatives, returning top {max_recommendations}")
        
        # Return top N recommendations
        return recommendations[:max_recommendations]


# Singleton instance
recommendation_service = RecommendationService()
