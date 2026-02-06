# Data Format Specification

## Parking History Data

### File: `data/raw/parking_history.csv`

**Format:**
```csv
date,zone_id,hour,occupancy
2025-01-01,1,0,25.5
2025-01-01,1,1,20.3
...
```

**Fields:**
- `date`: Date in YYYY-MM-DD format
- `zone_id`: Zone identifier (integer)
- `hour`: Hour of day (0-23)
- `occupancy`: Parking occupancy percentage (0-100)

## Traffic Data

### File: `data/raw/traffic_data.csv`

**Format:**
```csv
date,zone_id,hour,traffic_level
2025-01-01,1,0,low
2025-01-01,1,1,low
...
```

**Fields:**
- `date`: Date in YYYY-MM-DD format
- `zone_id`: Zone identifier (integer)
- `hour`: Hour of day (0-23)
- `traffic_level`: Traffic level (low, moderate, high)

## Events Data

### File: `data/raw/events.csv`

**Format:**
```csv
id,name,zone_id,date,start_time,end_time,expected_impact
1,Music Festival,1,2026-02-07,18:00,22:00,High
...
```

**Fields:**
- `id`: Event identifier (integer)
- `name`: Event name (string)
- `zone_id`: Zone identifier (integer)
- `date`: Event date in YYYY-MM-DD format
- `start_time`: Start time in HH:MM format
- `end_time`: End time in HH:MM format
- `expected_impact`: Expected parking impact (High, Medium, Low)

## Zones Configuration

### File: `data/processed/zones.json`

**Format:**
```json
[
  {
    "id": 1,
    "name": "Downtown",
    "lat": 40.7128,
    "lng": -74.0060,
    "description": "Zone description"
  }
]
```

**Fields:**
- `id`: Zone identifier (integer)
- `name`: Zone name (string)
- `lat`: Latitude (float)
- `lng`: Longitude (float)
- `description`: Zone description (string, optional)

## Processed Training Features

### File: `data/processed/training_features.csv`

**Format:**
```csv
hour,day_of_week,is_weekend,is_weekday,is_morning,is_afternoon,is_evening,is_night,is_rush_hour,month,day_of_month,is_business_district,is_shopping_area,is_residential,is_educational,traffic_impact,event_impact,events_count,occupancy
14,1,0,1,0,1,0,0,0,2,7,1,0,0,0,0.3,0.0,0,65.5
...
```

**Fields:**
- All feature columns (as listed above)
- `occupancy`: Target variable (0-100)
