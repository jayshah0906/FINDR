# Configuration for ML pipeline

# Zones to focus on (10 zones)
ZONES = [
    'BF_001',  # Downtown Pike St
    'BF_002',  # Downtown 1st Ave
    'BF_003',  # Downtown 3rd Ave
    'BF_045',  # Stadium District - Occidental
    'BF_046',  # Stadium District - 1st Ave S
    'BF_120',  # Capitol Hill - Broadway
    'BF_121',  # Capitol Hill - Pike St
    'BF_200',  # University District - University Way
    'BF_201',  # University District - 45th St
    'BF_202',  # Fremont - Fremont Ave
]

# Zone metadata
ZONE_METADATA = {
    'BF_001': {'name': 'Downtown Pike St', 'lat': 47.6062, 'lon': -122.3321, 'capacity': 20, 'type': 'commercial'},
    'BF_002': {'name': 'Downtown 1st Ave', 'lat': 47.6065, 'lon': -122.3340, 'capacity': 18, 'type': 'commercial'},
    'BF_003': {'name': 'Downtown 3rd Ave', 'lat': 47.6070, 'lon': -122.3360, 'capacity': 22, 'type': 'commercial'},
    'BF_045': {'name': 'Stadium District - Occidental', 'lat': 47.5952, 'lon': -122.3316, 'capacity': 35, 'type': 'event'},
    'BF_046': {'name': 'Stadium District - 1st Ave S', 'lat': 47.5948, 'lon': -122.3330, 'capacity': 30, 'type': 'event'},
    'BF_120': {'name': 'Capitol Hill - Broadway', 'lat': 47.6205, 'lon': -122.3212, 'capacity': 25, 'type': 'mixed'},
    'BF_121': {'name': 'Capitol Hill - Pike St', 'lat': 47.6145, 'lon': -122.3200, 'capacity': 20, 'type': 'mixed'},
    'BF_200': {'name': 'University District - University Way', 'lat': 47.6615, 'lon': -122.3132, 'capacity': 28, 'type': 'commercial'},
    'BF_201': {'name': 'University District - 45th St', 'lat': 47.6620, 'lon': -122.3140, 'capacity': 24, 'type': 'commercial'},
    'BF_202': {'name': 'Fremont - Fremont Ave', 'lat': 47.6505, 'lon': -122.3493, 'capacity': 18, 'type': 'mixed'},
}

# Feature names (15 features)
FEATURE_NAMES = [
    'hour',
    'day_of_week',
    'is_weekend',
    'month',
    'is_rush_hour',
    'avg_same_hour',
    'std_same_hour',
    'trend_24h',
    'occupancy_1h_ago',
    'occupancy_24h_ago',
    'occupancy_7d_ago',
    'has_event',
    'hours_until_event',
    'zone_type_encoded',
    'total_capacity'
]

# Zone type encoding
ZONE_TYPE_ENCODING = {
    'commercial': 0,
    'mixed': 1,
    'event': 2
}

# Model parameters
MODEL_PARAMS = {
    'n_estimators': 100,
    'max_depth': 15,
    'min_samples_split': 10,
    'random_state': 42,
    'n_jobs': -1
}

# Paths
DATA_RAW_PATH = 'ml/data/raw/'
DATA_PROCESSED_PATH = 'ml/data/processed/'
MODEL_PATH = 'ml/models/'
