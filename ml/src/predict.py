"""
Make predictions using trained model
"""
import joblib
import pandas as pd
from datetime import datetime, timedelta

from config import MODEL_PATH, ZONE_METADATA
from features import extract_all_features


# Load model once (global)
MODEL = None
HISTORICAL_DF = None
EVENTS_DF = None


def load_model():
    """Load trained model and data"""
    global MODEL, HISTORICAL_DF, EVENTS_DF
    
    if MODEL is None:
        import os
        import json
        
        # Get the directory of this script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        ml_dir = os.path.dirname(script_dir)
        
        print("Loading model...")
        model_path = os.path.join(ml_dir, 'models', 'parking_model.pkl')
        MODEL = joblib.load(model_path)
        
        print("Loading historical data...")
        data_path = os.path.join(ml_dir, 'data', 'processed', 'parking_data.json')
        HISTORICAL_DF = pd.read_json(data_path)
        HISTORICAL_DF['datetime'] = pd.to_datetime(HISTORICAL_DF['datetime'])
        
        print("Loading events...")
        events_path = os.path.join(ml_dir, 'data', 'processed', 'events.json')
        with open(events_path, 'r') as f:
            events_data = json.load(f)
        EVENTS_DF = pd.DataFrame(events_data)
        
        print("Model loaded successfully!")


def predict_occupancy(zone_id, hours_ahead=1):
    """
    Predict parking occupancy for a zone
    
    Args:
        zone_id: Zone identifier (e.g., 'BF_001')
        hours_ahead: Hours into the future (default: 1)
    
    Returns:
        dict with prediction results
    """
    # Load model if not already loaded
    load_model()
    
    # Calculate target datetime
    current_time = datetime.now()
    target_time = current_time + timedelta(hours=hours_ahead)
    
    # Extract features
    features = extract_all_features(
        zone_id,
        target_time,
        HISTORICAL_DF,
        EVENTS_DF
    )
    
    # Make prediction
    occupancy_rate = MODEL.predict([features])[0]
    
    # Ensure prediction is in valid range [0, 1]
    occupancy_rate = max(0.0, min(1.0, occupancy_rate))
    
    # Get zone metadata
    zone_info = ZONE_METADATA.get(zone_id, {})
    total_spaces = zone_info.get('capacity', 20)
    
    # Calculate availability
    availability_percent = (1 - occupancy_rate) * 100
    available_spaces = int((1 - occupancy_rate) * total_spaces)
    
    # Calculate confidence (simplified - based on prediction variance)
    # In production, you'd use prediction intervals from the forest
    confidence = 85  # Simplified for hackathon
    
    return {
        'zone_id': zone_id,
        'zone_name': zone_info.get('name', zone_id),
        'prediction_time': target_time.isoformat(),
        'occupancy_rate': float(occupancy_rate),
        'availability_percent': float(availability_percent),
        'available_spaces': available_spaces,
        'total_spaces': total_spaces,
        'confidence': confidence,
        'hours_ahead': hours_ahead
    }


def predict_multiple_zones(zone_ids, hours_ahead=1):
    """
    Predict for multiple zones at once
    
    Args:
        zone_ids: List of zone identifiers
        hours_ahead: Hours into the future
    
    Returns:
        list of prediction dicts
    """
    return [predict_occupancy(zone_id, hours_ahead) for zone_id in zone_ids]


def predict_time_series(zone_id, hours_list=[1, 2, 3, 4]):
    """
    Predict for multiple time points
    
    Args:
        zone_id: Zone identifier
        hours_list: List of hours ahead to predict
    
    Returns:
        list of predictions
    """
    return [predict_occupancy(zone_id, hours) for hours in hours_list]


# Test function
if __name__ == "__main__":
    print("Testing prediction function...")
    
    # Test single prediction
    result = predict_occupancy('BF_001', hours_ahead=1)
    
    print("\nPrediction Result:")
    print(f"  Zone: {result['zone_name']}")
    print(f"  Time: {result['prediction_time']}")
    print(f"  Occupancy: {result['occupancy_rate']:.2f} ({result['occupancy_rate']*100:.1f}%)")
    print(f"  Available: {result['availability_percent']:.1f}% ({result['available_spaces']} spaces)")
    print(f"  Confidence: {result['confidence']}%")
