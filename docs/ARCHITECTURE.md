# System Architecture

## Overview

The Parking Availability Prediction System is a full-stack application consisting of:
- **Backend**: FastAPI-based REST API
- **Frontend**: React-based web application
- **Data Layer**: SQLite database and CSV files

## Architecture Diagram

```
┌─────────────────┐
│   React Frontend │
│   (Port 5173)    │
└────────┬─────────┘
         │ HTTP/REST
         │
┌────────▼─────────┐
│  FastAPI Backend │
│   (Port 8000)    │
└────────┬─────────┘
         │
    ┌────┴────┐
    │         │
┌───▼───┐ ┌──▼──────┐
│ SQLite│ │ CSV Data│
│  DB   │ │  Files  │
└───────┘ └─────────┘
```

## Backend Architecture

### Structure
```
backend/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── config.py            # Configuration settings
│   ├── database.py          # Database connection
│   ├── models/              # Data models
│   ├── routes/              # API endpoints
│   ├── services/            # Business logic
│   ├── utils/               # Utility functions
│   └── middleware/          # Middleware (CORS, etc.)
├── scripts/                 # Utility scripts
├── tests/                   # Test files
└── requirements.txt         # Python dependencies
```

### Key Components

1. **Routes**: Handle HTTP requests and responses
2. **Services**: Contain business logic and prediction algorithms
3. **Models**: Define data structures and validation
4. **Utils**: Provide helper functions for time, traffic, events

### Prediction Flow

```
User Request
    │
    ▼
Route Handler (predict.py)
    │
    ▼
Prediction Service
    │
    ├──► Feature Builder
    │       ├── Time Utils
    │       ├── Traffic Utils
    │       └── Event Utils
    │
    ├──► Confidence Service
    │
    └──► ML Model / Rule-based
    │
    ▼
Response
```

## Frontend Architecture

### Structure
```
frontend/
├── src/
│   ├── components/          # Reusable UI components
│   ├── pages/               # Page components
│   ├── services/            # API client functions
│   ├── hooks/               # Custom React hooks
│   ├── utils/               # Utility functions
│   └── styles/              # CSS styles
├── public/                  # Static assets
└── package.json            # Dependencies
```

### Component Hierarchy

```
App
├── Header
└── Routes
    ├── Dashboard
    │   ├── MapView
    │   ├── ZoneSelector
    │   ├── TimePicker
    │   └── PredictionCard
    │       └── AvailabilityBadge
    └── ZoneDetail
        ├── TimePicker
        ├── Events List
        └── PredictionCard
```

## Data Flow

1. **User Input**: User selects zone, date, and time
2. **Frontend**: Sends prediction request to backend
3. **Backend**: 
   - Fetches zone and event data
   - Builds feature vector
   - Makes prediction using ML model or rule-based system
   - Calculates confidence score
4. **Response**: Returns prediction with availability level and confidence
5. **Frontend**: Displays prediction results

## Prediction Model

The system uses a hybrid approach:
- **Primary**: Machine Learning model (if available)
- **Fallback**: Rule-based prediction system

### Features Used
- Temporal: hour, day of week, month, is_weekend, is_rush_hour
- Zone-specific: zone type (business, shopping, residential, educational)
- Traffic: inferred traffic levels
- Events: nearby events and their impact

### Availability Levels
- **High**: Occupancy < 50%
- **Medium**: Occupancy 50-80%
- **Low**: Occupancy > 80%

## Technology Stack

### Backend
- **Framework**: FastAPI
- **Database**: SQLite (SQLAlchemy ORM)
- **ML**: scikit-learn (optional)
- **Validation**: Pydantic

### Frontend
- **Framework**: React 18
- **Build Tool**: Vite
- **Routing**: React Router
- **HTTP Client**: Axios
- **Styling**: CSS Modules

## Deployment Considerations

### Development
- Backend: `python run_server.py` (runs on port 8000)
- Frontend: `npm run dev` (runs on port 5173)

### Production
- Backend: Use production ASGI server (Gunicorn + Uvicorn)
- Frontend: Build static files (`npm run build`) and serve via Nginx
- Database: Consider PostgreSQL for production
- Caching: Add Redis for caching predictions
- Monitoring: Add logging and monitoring tools
