"""Initialize MongoDB database with collections and seed data."""
import asyncio
import sys
import os
from pathlib import Path
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Get the directory where this script is located
script_dir = Path(__file__).parent
env_path = script_dir / '.env'

# Load environment variables from .env file
load_dotenv(dotenv_path=env_path)

# Get DATABASE_URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    print(f"❌ ERROR: DATABASE_URL not found!")
    print(f"Looking for .env file at: {env_path}")
    print(f"File exists: {env_path.exists()}")
    sys.exit(1)

if "YOUR_PASSWORD_HERE" in DATABASE_URL:
    print("❌ ERROR: DATABASE_URL still contains placeholder!")
    print("Please edit backend/.env and replace YOUR_PASSWORD_HERE with your actual password.")
    sys.exit(1)


async def init_database():
    """Initialize MongoDB database."""
    print("🔄 Initializing MongoDB database...")
    print(f"📍 Connecting to: {DATABASE_URL[:50]}...")
    
    try:
        # Connect to MongoDB with SSL certificate handling for macOS
        import certifi
        client = AsyncIOMotorClient(
            DATABASE_URL,
            tlsCAFile=certifi.where()
        )
        db = client.get_database()
        
        # Test connection
        await db.command("ping")
        print("✅ Successfully connected to MongoDB!")
        
        # Create collections
        collections = await db.list_collection_names()
        
        if "users" not in collections:
            await db.create_collection("users")
            print("✅ Created 'users' collection")
        
        if "zones" not in collections:
            await db.create_collection("zones")
            print("✅ Created 'zones' collection")
        
        # Create indexes
        print("\n🔄 Creating indexes...")
        
        # User indexes
        await db.users.create_index("email", unique=True)
        await db.users.create_index("username", unique=True)
        print("✅ Created user indexes (email, username)")
        
        # Zone indexes
        await db.zones.create_index("id", unique=True)
        await db.zones.create_index("name", unique=True)
        print("✅ Created zone indexes (id, name)")
        
        # Seed zones
        print("\n🔄 Seeding default zones...")
        existing_zones = await db.zones.count_documents({})
        
        if existing_zones == 0:
            zones = [
                {"id": 1, "name": "Downtown Pike St", "latitude": 47.6105, "longitude": -122.3380, "description": "Downtown parking zone"},
                {"id": 2, "name": "Downtown 1st Ave", "latitude": 47.6050, "longitude": -122.3350, "description": "Downtown parking zone"},
                {"id": 3, "name": "Downtown 3rd Ave", "latitude": 47.6080, "longitude": -122.3310, "description": "Downtown parking zone"},
                {"id": 4, "name": "Capitol Hill - Broadway", "latitude": 47.6240, "longitude": -122.3210, "description": "Capitol Hill parking zone"},
                {"id": 5, "name": "University District - University Way", "latitude": 47.6650, "longitude": -122.3130, "description": "University District parking zone"},
                {"id": 6, "name": "Stadium District - Occidental", "latitude": 47.5920, "longitude": -122.3330, "description": "Stadium District parking zone"},
                {"id": 7, "name": "Stadium District - 1st Ave S", "latitude": 47.5970, "longitude": -122.3280, "description": "Stadium District parking zone"},
                {"id": 8, "name": "Capitol Hill - Pike St", "latitude": 47.6180, "longitude": -122.3150, "description": "Capitol Hill parking zone"},
                {"id": 9, "name": "University District - 45th St", "latitude": 47.6590, "longitude": -122.3080, "description": "University District parking zone"},
                {"id": 10, "name": "Fremont - Fremont Ave", "latitude": 47.6505, "longitude": -122.3493, "description": "Fremont parking zone"}
            ]
            
            await db.zones.insert_many(zones)
            print(f"✅ Seeded {len(zones)} zones")
        else:
            print(f"ℹ️  Zones already exist ({existing_zones} zones found)")
        
        # Summary
        print("\n" + "="*50)
        print("✅ MongoDB initialization complete!")
        print("="*50)
        print(f"📊 Users: {await db.users.count_documents({})} documents")
        print(f"📊 Zones: {await db.zones.count_documents({})} documents")
        print("="*50)
        
        client.close()
        
    except Exception as e:
        print(f"\n❌ Error initializing database: {e}")
        print("\n💡 Troubleshooting:")
        print("1. Check your DATABASE_URL in .env file")
        print("2. Verify MongoDB Atlas connection string is correct")
        print("3. Ensure IP whitelist includes your IP (0.0.0.0/0 for development)")
        print("4. Check database user credentials")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(init_database())
