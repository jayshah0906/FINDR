"""Import data from CSV files."""
import pandas as pd
import os
from app.config import settings


def import_parking_history():
    """Import parking history data."""
    csv_path = os.path.join(settings.RAW_DATA_DIR, "parking_history.csv")
    
    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        print("Creating sample data...")
        create_sample_data()
        return
    
    try:
        df = pd.read_csv(csv_path)
        print(f"Loaded {len(df)} records from parking_history.csv")
        return df
    except Exception as e:
        print(f"Error importing data: {e}")
        return None


def create_sample_data():
    """Create sample data files if they don't exist."""
    os.makedirs(settings.RAW_DATA_DIR, exist_ok=True)
    os.makedirs(settings.PROCESSED_DATA_DIR, exist_ok=True)
    
    # Create sample parking history
    import numpy as np
    from datetime import datetime, timedelta
    
    dates = []
    zones = []
    hours = []
    occupancies = []
    
    start_date = datetime(2025, 1, 1)
    for day in range(365):
        date = start_date + timedelta(days=day)
        for zone_id in range(1, 6):
            for hour in range(24):
                dates.append(date.strftime("%Y-%m-%d"))
                zones.append(zone_id)
                hours.append(hour)
                # Generate realistic occupancy based on patterns
                base = 50 + np.sin(hour * np.pi / 12) * 20
                if zone_id in [1, 2]:  # Business districts
                    base += 20
                if date.weekday() < 5:  # Weekday
                    base += 10
                occupancy = max(0, min(100, base + np.random.normal(0, 10)))
                occupancies.append(round(occupancy, 1))
    
    df = pd.DataFrame({
        "date": dates,
        "zone_id": zones,
        "hour": hours,
        "occupancy": occupancies
    })
    
    csv_path = os.path.join(settings.RAW_DATA_DIR, "parking_history.csv")
    df.to_csv(csv_path, index=False)
    print(f"Created sample parking_history.csv with {len(df)} records")


if __name__ == "__main__":
    import_parking_history()
