"""
Create events for DEMO DAY ONLY
Simple approach for hackathon
"""
import json
from datetime import datetime, timedelta

def create_demo_events():
    """
    Create events for the demo day
    This makes the demo more realistic without needing a full calendar
    """
    
    # Get demo date (you can change this to your actual demo date)
    demo_date = "2026-02-06"  # Change to your hackathon demo date
    
    events = [
        {
            "event_id": "DEMO_001",
            "event_name": "Seahawks Playoff Game",
            "event_type": "sports",
            "venue": "Lumen Field",
            "date": demo_date,
            "start_time": "19:00",  # 7 PM
            "expected_attendance": 68000,
            "nearby_zones": ["BF_045", "BF_046"],
            "impact_level": "very_high",
            "description": "Major playoff game - expect very high parking demand"
        },
        {
            "event_id": "DEMO_002",
            "event_name": "Tech Conference Downtown",
            "event_type": "conference",
            "venue": "Washington State Convention Center",
            "date": demo_date,
            "start_time": "09:00",  # 9 AM
            "expected_attendance": 5000,
            "nearby_zones": ["BF_001", "BF_002", "BF_003"],
            "impact_level": "medium",
            "description": "All-day conference - moderate parking impact"
        },
        {
            "event_id": "DEMO_003",
            "event_name": "Capitol Hill Art Walk",
            "event_type": "festival",
            "venue": "Capitol Hill",
            "date": demo_date,
            "start_time": "18:00",  # 6 PM
            "expected_attendance": 3000,
            "nearby_zones": ["BF_120", "BF_121"],
            "impact_level": "medium",
            "description": "Evening art walk - moderate parking impact"
        }
    ]
    
    return events


def save_demo_events(events):
    """Save demo events to JSON"""
    
    output_file = 'ml/data/processed/events.json'
    
    with open(output_file, 'w') as f:
        json.dump(events, f, indent=2)
    
    print("="*60)
    print("DEMO EVENTS CREATED")
    print("="*60)
    print(f"\n✅ Created {len(events)} events for demo day")
    print(f"📁 Saved to: {output_file}")
    print("\n📋 Events:")
    for event in events:
        print(f"\n  {event['event_name']}")
        print(f"    Date: {event['date']}")
        print(f"    Time: {event['start_time']}")
        print(f"    Zones affected: {', '.join(event['nearby_zones'])}")
        print(f"    Impact: {event['impact_level']}")
    
    print("\n" + "="*60)
    print("DEMO SCENARIOS")
    print("="*60)
    print("\n1. Stadium District (BF_045, BF_046)")
    print("   → Show HIGH occupancy due to Seahawks game")
    print("\n2. Downtown (BF_001, BF_002, BF_003)")
    print("   → Show MEDIUM occupancy due to conference")
    print("\n3. Capitol Hill (BF_120, BF_121)")
    print("   → Show MEDIUM occupancy due to art walk")
    print("\n4. Other zones")
    print("   → Show NORMAL occupancy (no events)")
    print("\n" + "="*60)


def main():
    """Create demo events"""
    print("\n🎯 Creating events for DEMO DAY ONLY")
    print("This is simpler and more realistic for hackathon demo\n")
    
    events = create_demo_events()
    save_demo_events(events)
    
    print("\n💡 TIP: Change the date in this file to match your demo date!")
    print("📝 File: ml/src/create_demo_events.py")
    print("🔧 Line: demo_date = '2026-02-06'  # Change this!\n")


if __name__ == "__main__":
    main()
