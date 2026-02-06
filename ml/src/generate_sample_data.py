"""
Generate sample parking data for testing
(Use this until you download real Seattle data)
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

from config import ZONES, ZONE_METADATA


def generate_parking_data(start_date='2023-01-01', end_date='2024-12-31'):
    """
    Generate synthetic parking data with realistic patterns
    """
    print("Generating sample parking data...")
    
    data = []
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    current = start
    while current <= end:
        for zone_id in ZONES:
            zone_info = ZONE_METADATA[zone_id]
            capacity = zone_info['capacity']
            zone_type = zone_info['type']
            
            # Base occupancy by zone type
            if zone_type == 'commercial':
                base_occupancy = 0.65
            elif zone_type == 'event':
                base_occupancy = 0.55
            else:  # mixed
                base_occupancy = 0.60
            
            # Time of day pattern
            hour = current.hour
            if 7 <= hour <= 9:  # Morning rush
                time_factor = 0.25
            elif 11 <= hour <= 14:  # Lunch
                time_factor = 0.15
            elif 17 <= hour <= 19:  # Evening rush
                time_factor = 0.30
            elif 20 <= hour <= 6:  # Night
                time_factor = -0.30
            else:
                time_factor = 0.0
            
            # Day of week pattern
            if current.weekday() < 5:  # Weekday
                dow_factor = 0.10
            elif current.weekday() == 5:  # Saturday
                dow_factor = 0.05
            else:  # Sunday
                dow_factor = -0.15
            
            # Calculate occupancy
            occupancy_rate = base_occupancy + time_factor + dow_factor
            
            # Add some randomness
            occupancy_rate += np.random.normal(0, 0.08)
            
            # Clip to valid range
            occupancy_rate = max(0.05, min(0.98, occupancy_rate))
            
            # Calculate spaces
            occupied_spaces = int(occupancy_rate * capacity)
            
            data.append({
                'blockface_id': zone_id,
                'datetime': current.isoformat(),
                'occupied_spaces': occupied_spaces,
                'total_spaces': capacity,
                'occupancy_rate': round(occupancy_rate, 3)
            })
        
        # Move to next hour
        current += timedelta(hours=1)
    
    df = pd.DataFrame(data)
    print(f"Generated {len(df)} records")
    return df


def generate_events():
    """Generate sample events"""
    print("Generating sample events...")
    
    events = [
        # Seahawks games (home games)
        {'event_id': 'E001', 'event_name': 'Seahawks vs 49ers', 'date': '2024-09-15', 'start_time': '13:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E002', 'event_name': 'Seahawks vs Rams', 'date': '2024-09-22', 'start_time': '13:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E003', 'event_name': 'Seahawks vs Cardinals', 'date': '2024-10-06', 'start_time': '13:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E004', 'event_name': 'Seahawks vs Giants', 'date': '2024-10-13', 'start_time': '16:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E005', 'event_name': 'Seahawks vs Bills', 'date': '2024-10-27', 'start_time': '13:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E006', 'event_name': 'Seahawks vs Packers', 'date': '2024-11-03', 'start_time': '16:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E007', 'event_name': 'Seahawks vs Vikings', 'date': '2024-11-17', 'start_time': '13:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E008', 'event_name': 'Seahawks vs Bears', 'date': '2024-12-01', 'start_time': '16:00', 'nearby_zones': ['BF_045', 'BF_046']},
        
        # Mariners games (sample)
        {'event_id': 'E009', 'event_name': 'Mariners Opening Day', 'date': '2024-03-28', 'start_time': '19:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E010', 'event_name': 'Mariners vs Yankees', 'date': '2024-05-15', 'start_time': '19:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E011', 'event_name': 'Mariners vs Red Sox', 'date': '2024-06-20', 'start_time': '19:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E012', 'event_name': 'Mariners vs Dodgers', 'date': '2024-07-04', 'start_time': '13:00', 'nearby_zones': ['BF_045', 'BF_046']},
        {'event_id': 'E013', 'event_name': 'Mariners vs Astros', 'date': '2024-08-10', 'start_time': '19:00', 'nearby_zones': ['BF_045', 'BF_046']},
        
        # Other events
        {'event_id': 'E014', 'event_name': 'Capitol Hill Block Party', 'date': '2024-07-20', 'start_time': '12:00', 'nearby_zones': ['BF_120', 'BF_121']},
        {'event_id': 'E015', 'event_name': 'University District Street Fair', 'date': '2024-05-18', 'start_time': '10:00', 'nearby_zones': ['BF_200', 'BF_201']},
    ]
    
    df = pd.DataFrame(events)
    print(f"Generated {len(df)} events")
    return df


def save_data(parking_df, events_df):
    """Save data to JSON files"""
    print("\nSaving data...")
    
    # Save parking data
    parking_file = 'ml/data/processed/parking_data.json'
    parking_df.to_json(parking_file, orient='records', date_format='iso')
    print(f"Saved parking data: {parking_file}")
    
    # Save events
    events_file = 'ml/data/processed/events.json'
    events_df.to_json(events_file, orient='records')
    print(f"Saved events: {events_file}")
    
    # Save zone metadata
    zones_file = 'ml/data/processed/zones_metadata.json'
    with open(zones_file, 'w') as f:
        json.dump(ZONE_METADATA, f, indent=2)
    print(f"Saved zone metadata: {zones_file}")


def main():
    """Generate all sample data"""
    print("="*60)
    print("GENERATING SAMPLE DATA")
    print("="*60)
    print("\nNote: This is synthetic data for testing.")
    print("Replace with real Seattle data when available.\n")
    
    # Generate data
    parking_df = generate_parking_data('2023-01-01', '2024-12-31')
    events_df = generate_events()
    
    # Save
    save_data(parking_df, events_df)
    
    print("\n" + "="*60)
    print("DATA GENERATION COMPLETE!")
    print("="*60)
    print("\nYou can now run: python ml/src/train.py")


if __name__ == "__main__":
    main()
