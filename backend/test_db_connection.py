"""Test MongoDB connection and verify database setup."""
import asyncio
import sys
import os
from motor.motor_asyncio import AsyncIOMotorClient
import certifi
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Colors for terminal output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'


async def test_connection():
    """Test MongoDB connection."""
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}MongoDB Connection Test{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")
    
    # Get DATABASE_URL
    database_url = os.getenv("DATABASE_URL")
    
    if not database_url:
        print(f"{RED}❌ ERROR: DATABASE_URL not found in environment variables{RESET}")
        print(f"{YELLOW}Please set DATABASE_URL in .env file or environment{RESET}")
        return False
    
    # Mask password in output
    masked_url = database_url
    if "@" in database_url:
        parts = database_url.split("@")
        if ":" in parts[0]:
            user_pass = parts[0].split("://")[1]
            username = user_pass.split(":")[0]
            masked_url = database_url.replace(user_pass, f"{username}:****")
    
    print(f"{BLUE}1. Checking DATABASE_URL...{RESET}")
    print(f"   URL: {masked_url}")
    
    if database_url.startswith("mongodb://localhost"):
        print(f"{YELLOW}   ⚠️  Using local MongoDB (not Atlas){RESET}")
    elif database_url.startswith("mongodb+srv://"):
        print(f"{GREEN}   ✅ Using MongoDB Atlas{RESET}")
    else:
        print(f"{RED}   ❌ Invalid MongoDB URL format{RESET}")
        return False
    
    # Test connection
    print(f"\n{BLUE}2. Testing connection...{RESET}")
    try:
        client = AsyncIOMotorClient(
            database_url,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=5000
        )
        
        # Ping the database
        await client.admin.command('ping')
        print(f"{GREEN}   ✅ Successfully connected to MongoDB!{RESET}")
        
        # Get database
        db = client.get_database()
        db_name = db.name
        print(f"{GREEN}   ✅ Database name: {db_name}{RESET}")
        
        # List collections
        print(f"\n{BLUE}3. Checking collections...{RESET}")
        collections = await db.list_collection_names()
        
        if collections:
            print(f"{GREEN}   ✅ Found {len(collections)} collections:{RESET}")
            for coll in collections:
                count = await db[coll].count_documents({})
                print(f"      - {coll}: {count} documents")
        else:
            print(f"{YELLOW}   ⚠️  No collections found (database is empty){RESET}")
        
        # Check required collections
        print(f"\n{BLUE}4. Checking required collections...{RESET}")
        required_collections = ["users", "zones"]
        
        for coll_name in required_collections:
            if coll_name in collections:
                count = await db[coll_name].count_documents({})
                print(f"{GREEN}   ✅ {coll_name}: {count} documents{RESET}")
            else:
                print(f"{YELLOW}   ⚠️  {coll_name}: Not found (will be created on first use){RESET}")
        
        # Test zones collection
        print(f"\n{BLUE}5. Testing zones collection...{RESET}")
        zones_count = await db.zones.count_documents({})
        
        if zones_count == 0:
            print(f"{YELLOW}   ⚠️  Zones collection is empty{RESET}")
            print(f"{YELLOW}   💡 Run: python backend/scripts/seed_zones.py{RESET}")
        else:
            print(f"{GREEN}   ✅ Found {zones_count} zones{RESET}")
            
            # Show first zone
            first_zone = await db.zones.find_one()
            if first_zone:
                print(f"      Sample zone: {first_zone.get('name', 'N/A')}")
        
        # Test users collection
        print(f"\n{BLUE}6. Testing users collection...{RESET}")
        users_count = await db.users.count_documents({})
        print(f"   Users: {users_count}")
        
        # Test indexes
        print(f"\n{BLUE}7. Checking indexes...{RESET}")
        try:
            user_indexes = await db.users.index_information()
            zone_indexes = await db.zones.index_information()
            print(f"{GREEN}   ✅ Users indexes: {len(user_indexes)}{RESET}")
            print(f"{GREEN}   ✅ Zones indexes: {len(zone_indexes)}{RESET}")
        except Exception as e:
            print(f"{YELLOW}   ⚠️  Could not check indexes: {e}{RESET}")
        
        # Close connection
        client.close()
        
        print(f"\n{GREEN}{'='*60}{RESET}")
        print(f"{GREEN}✅ All tests passed! Database connection is working.{RESET}")
        print(f"{GREEN}{'='*60}{RESET}\n")
        
        return True
        
    except Exception as e:
        print(f"{RED}   ❌ Connection failed: {e}{RESET}")
        print(f"\n{RED}{'='*60}{RESET}")
        print(f"{RED}❌ Database connection test failed{RESET}")
        print(f"{RED}{'='*60}{RESET}\n")
        
        print(f"{YELLOW}Common issues:{RESET}")
        print(f"1. Check DATABASE_URL is correct")
        print(f"2. Check MongoDB Atlas Network Access allows your IP")
        print(f"3. Check username/password are correct")
        print(f"4. Check database name is correct")
        print(f"5. Check internet connection")
        
        return False


async def seed_zones_if_empty():
    """Seed zones if collection is empty."""
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        return
    
    try:
        client = AsyncIOMotorClient(database_url, tlsCAFile=certifi.where())
        db = client.get_database()
        
        zones_count = await db.zones.count_documents({})
        
        if zones_count == 0:
            print(f"\n{BLUE}Seeding zones...{RESET}")
            
            zones = [
                {"id": 1, "name": "Downtown Pike St", "lat": 47.6105, "lng": -122.3380},
                {"id": 2, "name": "Downtown 1st Ave", "lat": 47.6050, "lng": -122.3350},
                {"id": 3, "name": "Downtown 3rd Ave", "lat": 47.6080, "lng": -122.3310},
                {"id": 4, "name": "Capitol Hill - Broadway", "lat": 47.6240, "lng": -122.3210},
                {"id": 5, "name": "University District - University Way", "lat": 47.6650, "lng": -122.3130},
                {"id": 6, "name": "Stadium District - Occidental", "lat": 47.5920, "lng": -122.3330},
                {"id": 7, "name": "Stadium District - 1st Ave S", "lat": 47.5970, "lng": -122.3280},
                {"id": 8, "name": "Capitol Hill - Pike St", "lat": 47.6180, "lng": -122.3150},
                {"id": 9, "name": "University District - 45th St", "lat": 47.6590, "lng": -122.3080},
                {"id": 10, "name": "Fremont - Fremont Ave", "lat": 47.6505, "lng": -122.3493},
            ]
            
            await db.zones.insert_many(zones)
            print(f"{GREEN}✅ Seeded {len(zones)} zones{RESET}")
        
        client.close()
        
    except Exception as e:
        print(f"{RED}❌ Failed to seed zones: {e}{RESET}")


if __name__ == "__main__":
    # Run tests
    success = asyncio.run(test_connection())
    
    if success:
        # Seed zones if needed
        asyncio.run(seed_zones_if_empty())
        sys.exit(0)
    else:
        sys.exit(1)
