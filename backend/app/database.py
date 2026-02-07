"""MongoDB database connection and session management."""
import motor.motor_asyncio
import certifi
from app.config import settings

# Global client variable
_client = None
_database = None


def get_client():
    """Get or create MongoDB client."""
    global _client
    if _client is None:
        _client = motor.motor_asyncio.AsyncIOMotorClient(
            settings.DATABASE_URL,
            tlsCAFile=certifi.where()
        )
    return _client


def get_database():
    """Get database instance."""
    global _database
    if _database is None:
        client = get_client()
        _database = client.get_database()
    return _database


# Collections (lazy loaded)
@property
def users_collection():
    return get_database().get_collection("users")


@property
def zones_collection():
    return get_database().get_collection("zones")


# For backward compatibility
database = get_database()
users_collection = database.get_collection("users")
zones_collection = database.get_collection("zones")


async def get_db():
    """Dependency to get database (for compatibility with existing code)."""
    return get_database()


# Helper functions for MongoDB operations
async def create_indexes():
    """Create indexes for collections."""
    db = get_database()
    
    # User indexes
    await db.users.create_index("email", unique=True)
    await db.users.create_index("username", unique=True)
    
    # Zone indexes
    await db.zones.create_index("name", unique=True)
    await db.zones.create_index("id", unique=True)
    
    print("✅ MongoDB indexes created successfully")


async def close_db_connection():
    """Close database connection."""
    global _client
    if _client:
        _client.close()
        _client = None
