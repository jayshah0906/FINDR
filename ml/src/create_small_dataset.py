"""
Create a small dataset for quick testing
"""
import json
import pandas as pd
from datetime import datetime, timedelta

print("Creating small dataset for testing...")

# Load full parking data
with open('ml/data/processed/parking_data.json', 'r') as f:
    full_data = json.load(f)

# Take only first 1000 records
small_data = full_data[:1000]

# Save small dataset
with open('ml/data/processed/parking_data_small.json', 'w') as f:
    json.dump(small_data, f, indent=2)

print(f"✅ Created small dataset with {len(small_data)} records")
print(f"📁 Saved to: ml/data/processed/parking_data_small.json")

# Show date range
df = pd.DataFrame(small_data)
df['datetime'] = pd.to_datetime(df['datetime'])
print(f"\nDate range: {df['datetime'].min()} to {df['datetime'].max()}")
print(f"Zones: {df['blockface_id'].nunique()} unique zones")
