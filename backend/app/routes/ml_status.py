"""ML model status and validation routes."""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Dict, List
import os
from app.services.prediction_service import prediction_service
from app.config import settings

router = APIRouter()


class MLStatusResponse(BaseModel):
    """Response model for ML status."""
    ml_available: bool
    ml_model_path: str
    ml_model_exists: bool
    ml_model_size_mb: float
    ml_data_dir: str
    ml_data_exists: bool
    use_ml_model_config: bool
    zone_mappings: Dict[int, str]
    total_zones: int
    status_message: str
    recommendations: List[str]


@router.get("/ml-status", response_model=MLStatusResponse)
async def get_ml_status():
    """
    Get ML model status and configuration.
    
    This endpoint validates that the ML model is properly loaded and configured
    for use in predictions and recommendations.
    """
    ml_model_path = settings.ML_MODEL_PATH
    ml_data_dir = settings.ML_DATA_DIR
    
    # Check if files exist
    model_exists = os.path.isfile(ml_model_path)
    data_exists = os.path.isdir(ml_data_dir)
    
    # Get model size if it exists
    model_size_mb = 0.0
    if model_exists:
        model_size_mb = os.path.getsize(ml_model_path) / (1024 * 1024)
    
    # Determine status
    ml_available = prediction_service.ml_available
    
    # Generate status message
    if ml_available:
        status_message = "✅ ML model is ACTIVE and being used for all predictions"
    elif not settings.USE_ML_MODEL:
        status_message = "⚠️  ML model is DISABLED in configuration (USE_ML_MODEL=false)"
    elif not model_exists:
        status_message = f"❌ ML model file NOT FOUND at: {ml_model_path}"
    elif not data_exists:
        status_message = f"❌ ML data directory NOT FOUND at: {ml_data_dir}"
    else:
        status_message = "❌ ML model failed to load (check server logs for details)"
    
    # Generate recommendations
    recommendations = []
    if not ml_available:
        if not settings.USE_ML_MODEL:
            recommendations.append("Set USE_ML_MODEL=true in environment or .env file")
        if not model_exists:
            recommendations.append(f"Ensure ML model exists at: {ml_model_path}")
            recommendations.append("Run: cd ml && python src/train.py")
        if not data_exists:
            recommendations.append(f"Ensure ML data directory exists at: {ml_data_dir}")
            recommendations.append("Run: cd ml && python scripts/prepare_data.py")
        if model_exists and data_exists and settings.USE_ML_MODEL:
            recommendations.append("Check server logs for ML model loading errors")
            recommendations.append("Restart the backend server")
    else:
        recommendations.append("ML model is working correctly!")
        recommendations.append(f"Model size: {model_size_mb:.1f} MB")
        recommendations.append(f"Configured for {len(settings.ML_ZONE_ID_MAP)} zones")
    
    return MLStatusResponse(
        ml_available=ml_available,
        ml_model_path=ml_model_path,
        ml_model_exists=model_exists,
        ml_model_size_mb=round(model_size_mb, 2),
        ml_data_dir=ml_data_dir,
        ml_data_exists=data_exists,
        use_ml_model_config=settings.USE_ML_MODEL,
        zone_mappings=settings.ML_ZONE_ID_MAP,
        total_zones=len(settings.ML_ZONE_ID_MAP),
        status_message=status_message,
        recommendations=recommendations
    )


@router.get("/ml-test")
async def test_ml_prediction():
    """
    Test ML prediction with a sample zone and time.
    
    This endpoint makes a real ML prediction to verify the model is working.
    """
    try:
        # Test prediction for Zone 1 at 6 PM on a weekday
        result = prediction_service.predict_occupancy(
            zone_id=1,
            date_str="2024-12-25",
            hour=18,
            day_of_week=2,  # Wednesday
            events=[]
        )
        
        ml_used = result.get("ml_used", False)
        
        return {
            "success": True,
            "ml_used": ml_used,
            "test_zone": "Zone 1 (Downtown Pike St)",
            "test_time": "2024-12-25 18:00 (Wednesday)",
            "prediction": {
                "occupancy": result["occupancy"],
                "availability_level": result["availability_level"],
                "confidence": result["confidence"]
            },
            "message": "✅ ML prediction successful!" if ml_used else "⚠️  Fallback prediction used (ML not active)"
        }
    except Exception as e:
        return {
            "success": False,
            "ml_used": False,
            "error": str(e),
            "message": "❌ ML prediction failed"
        }
