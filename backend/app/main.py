"""Main FastAPI application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import zones, predict, events, health
from app.middleware.cors import setup_cors

# Create FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description="AI-powered parking availability prediction system"
)

# Setup CORS
setup_cors(app)

# Include routers
app.include_router(health.router, prefix=settings.API_PREFIX, tags=["Health"])
app.include_router(zones.router, prefix=settings.API_PREFIX, tags=["Zones"])
app.include_router(predict.router, prefix=settings.API_PREFIX, tags=["Predictions"])
app.include_router(events.router, prefix=settings.API_PREFIX, tags=["Events"])


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Parking Availability Prediction API",
        "version": settings.API_VERSION,
        "docs": "/docs"
    }
