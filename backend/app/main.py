"""Main FastAPI application."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.config import settings
from app.routes import zones, predict, events, health, auth_routes, recommendations, ml_status
from app.middleware.cors import setup_cors
from app.database import create_indexes, close_db_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan context manager for startup and shutdown events."""
    # Startup
    print("🔄 Starting up application...")
    try:
        await create_indexes()
        print("✅ MongoDB indexes created")
    except Exception as e:
        print(f"⚠️  Warning: Could not create indexes: {e}")
    
    yield
    
    # Shutdown
    print("🔄 Shutting down application...")
    await close_db_connection()
    print("✅ MongoDB connection closed")


# Create FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    description="AI-powered parking availability prediction system",
    lifespan=lifespan
)

# Setup CORS
setup_cors(app)

# Include routers
app.include_router(health.router, prefix=settings.API_PREFIX, tags=["Health"])
app.include_router(ml_status.router, prefix=settings.API_PREFIX, tags=["ML Status"])
app.include_router(auth_routes.router, prefix=settings.API_PREFIX, tags=["Authentication"])
app.include_router(zones.router, prefix=settings.API_PREFIX, tags=["Zones"])
app.include_router(predict.router, prefix=settings.API_PREFIX, tags=["Predictions"])
app.include_router(events.router, prefix=settings.API_PREFIX, tags=["Events"])
app.include_router(recommendations.router, prefix=settings.API_PREFIX, tags=["Recommendations"])


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Parking Availability Prediction API",
        "version": settings.API_VERSION,
        "docs": "/docs"
    }
