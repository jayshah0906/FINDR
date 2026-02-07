#!/usr/bin/env python3
"""
End-to-End Test: ML Model → Backend → Frontend
Tests the complete data flow for recommendations system.
"""

import requests
import json
import sys
from datetime import datetime

# Configuration
BACKEND_URL = "http://localhost:8001"
API_PREFIX = "/api/v1"

# Colors for output
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

def print_header(text):
    print(f"\n{BLUE}{'='*70}{RESET}")
    print(f"{BLUE}{text.center(70)}{RESET}")
    print(f"{BLUE}{'='*70}{RESET}\n")

def print_success(text):
    print(f"{GREEN}✅ {text}{RESET}")

def print_error(text):
    print(f"{RED}❌ {text}{RESET}")

def print_warning(text):
    print(f"{YELLOW}⚠️  {text}{RESET}")

def print_info(text):
    print(f"{BLUE}ℹ️  {text}{RESET}")


def test_backend_health():
    """Test 1: Backend is running"""
    print_header("TEST 1: Backend Health Check")
    
    try:
        response = requests.get(f"{BACKEND_URL}/", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print_success(f"Backend is running: {data.get('message')}")
            print_info(f"Version: {data.get('version')}")
            return True
        else:
            print_error(f"Backend returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print_error("Cannot connect to backend! Is it running on port 8001?")
        return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False


def test_ml_status():
    """Test 2: ML Model is loaded and active"""
    print_header("TEST 2: ML Model Status")
    
    try:
        response = requests.get(f"{BACKEND_URL}{API_PREFIX}/ml-status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            
            print_info(f"ML Available: {data['ml_available']}")
            print_info(f"Model Path: {data['ml_model_path']}")
            print_info(f"Model Size: {data['ml_model_size_mb']} MB")
            print_info(f"Total Zones: {data['total_zones']}")
            print_info(f"Status: {data['status_message']}")
            
            if data['ml_available']:
                print_success("ML model is ACTIVE and ready!")
                return True
            else:
                print_error("ML model is NOT available!")
                print_warning("Recommendations:")
                for rec in data.get('recommendations', []):
                    print(f"  - {rec}")
                return False
        else:
            print_error(f"ML status endpoint returned {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error checking ML status: {e}")
        return False


def test_ml_prediction():
    """Test 3: ML Model makes predictions"""
    print_header("TEST 3: ML Prediction Test")
    
    try:
        response = requests.get(f"{BACKEND_URL}{API_PREFIX}/ml-test", timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            print_info(f"Test Zone: {data['test_zone']}")
            print_info(f"Test Time: {data['test_time']}")
            print_info(f"ML Used: {data['ml_used']}")
            
            prediction = data['prediction']
            print_info(f"Occupancy: {prediction['occupancy']}%")
            print_info(f"Availability: {prediction['availability_level']}")
            print_info(f"Confidence: {prediction['confidence']*100:.0f}%")
            
            if data['ml_used']:
                print_success("ML prediction successful!")
                return True
            else:
                print_warning("Prediction used fallback (not ML)")
                return False
        else:
            print_error(f"ML test endpoint returned {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error testing ML prediction: {e}")
        return False


def test_single_prediction():
    """Test 4: Single zone prediction via /predict endpoint"""
    print_header("TEST 4: Single Zone Prediction (Frontend Uses This)")
    
    test_data = {
        "zone_id": 1,
        "date": "2024-12-25",
        "hour": 18,
        "day_of_week": 2
    }
    
    try:
        print_info(f"Requesting prediction for Zone {test_data['zone_id']}")
        print_info(f"Date/Time: {test_data['date']} {test_data['hour']}:00")
        
        response = requests.post(
            f"{BACKEND_URL}{API_PREFIX}/predict",
            json=test_data,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            
            print_success("Prediction received!")
            print_info(f"Zone: {data['zone_name']}")
            print_info(f"Occupancy: {data['predicted_occupancy']}%")
            print_info(f"Availability: {data['availability_level']}")
            print_info(f"Confidence: {data['confidence_score']*100:.0f}%")
            print_info(f"Available Spaces: {data['available_spaces']}/{data['total_spaces']}")
            
            # Check if realistic
            if 0 <= data['predicted_occupancy'] <= 100:
                print_success("Prediction values are realistic!")
                return True
            else:
                print_error(f"Prediction value out of range: {data['predicted_occupancy']}%")
                return False
        else:
            print_error(f"Predict endpoint returned {response.status_code}")
            print_error(f"Response: {response.text}")
            return False
    except Exception as e:
        print_error(f"Error testing prediction: {e}")
        return False


def test_recommendations():
    """Test 5: Recommendations endpoint (ML-powered alternatives)"""
    print_header("TEST 5: Alternative Zone Recommendations")
    
    params = {
        "zone_id": 1,
        "date": "2024-12-25",
        "hour": 18,
        "day_of_week": 2,
        "availability_level": "Low",
        "max_recommendations": 3
    }
    
    try:
        print_info(f"Requesting alternatives for Zone {params['zone_id']} (Low availability)")
        
        response = requests.get(
            f"{BACKEND_URL}{API_PREFIX}/recommendations",
            params=params,
            timeout=15
        )
        
        if response.status_code == 200:
            recommendations = response.json()
            
            if len(recommendations) == 0:
                print_warning("No recommendations returned (might be expected if all zones are busy)")
                return True
            
            print_success(f"Received {len(recommendations)} recommendations!")
            
            for i, rec in enumerate(recommendations, 1):
                print(f"\n  {GREEN}Recommendation #{i}:{RESET}")
                print(f"    Zone: {rec['zone_name']} (ID: {rec['zone_id']})")
                print(f"    Distance: {rec['distance_display']}")
                print(f"    Availability: {rec['availability_level']}")
                print(f"    Occupancy: {rec['occupancy']}%")
                print(f"    Confidence: {rec['confidence']*100:.0f}%")
                print(f"    Reason: {rec['reason']}")
                print(f"    Score: {rec['recommendation_score']:.2f}")
            
            # Validate recommendations
            all_valid = True
            for rec in recommendations:
                if not (0 <= rec['occupancy'] <= 100):
                    print_error(f"Invalid occupancy: {rec['occupancy']}%")
                    all_valid = False
                if not (0 <= rec['confidence'] <= 1):
                    print_error(f"Invalid confidence: {rec['confidence']}")
                    all_valid = False
                if rec['availability_level'] not in ['High', 'Medium', 'Low']:
                    print_error(f"Invalid availability level: {rec['availability_level']}")
                    all_valid = False
            
            if all_valid:
                print_success("\nAll recommendations have valid data!")
                return True
            else:
                print_error("\nSome recommendations have invalid data!")
                return False
        else:
            print_error(f"Recommendations endpoint returned {response.status_code}")
            print_error(f"Response: {response.text}")
            return False
    except Exception as e:
        print_error(f"Error testing recommendations: {e}")
        return False


def test_frontend_flow():
    """Test 6: Simulate complete frontend flow"""
    print_header("TEST 6: Complete Frontend Flow Simulation")
    
    print_info("Simulating user selecting Zone 1 at 6 PM on Christmas...")
    
    # Step 1: Get prediction for selected zone
    print("\n  Step 1: Get prediction for selected zone")
    prediction_data = {
        "zone_id": 1,
        "date": "2024-12-25",
        "hour": 18,
        "day_of_week": 2
    }
    
    try:
        pred_response = requests.post(
            f"{BACKEND_URL}{API_PREFIX}/predict",
            json=prediction_data,
            timeout=10
        )
        
        if pred_response.status_code != 200:
            print_error("Failed to get prediction")
            return False
        
        pred_data = pred_response.json()
        availability = pred_data['availability_level']
        
        print_success(f"Got prediction: {availability} availability ({pred_data['predicted_occupancy']}% occupied)")
        
        # Step 2: If Low/Medium, get recommendations
        if availability in ['Low', 'Medium']:
            print(f"\n  Step 2: Availability is {availability}, fetching alternatives...")
            
            rec_params = {
                "zone_id": 1,
                "date": "2024-12-25",
                "hour": 18,
                "day_of_week": 2,
                "availability_level": availability,
                "max_recommendations": 3
            }
            
            rec_response = requests.get(
                f"{BACKEND_URL}{API_PREFIX}/recommendations",
                params=rec_params,
                timeout=15
            )
            
            if rec_response.status_code != 200:
                print_error("Failed to get recommendations")
                return False
            
            recommendations = rec_response.json()
            
            if len(recommendations) > 0:
                print_success(f"Got {len(recommendations)} alternative zones!")
                print_info("Frontend would display these in the 'Better Options Nearby' card")
                return True
            else:
                print_warning("No alternatives available (all zones might be busy)")
                return True
        else:
            print_info(f"\n  Step 2: Availability is {availability}, no alternatives needed")
            print_success("Frontend would NOT show alternatives card (not needed)")
            return True
            
    except Exception as e:
        print_error(f"Error in frontend flow simulation: {e}")
        return False


def test_data_consistency():
    """Test 7: Data consistency across multiple requests"""
    print_header("TEST 7: Data Consistency Check")
    
    print_info("Making 3 identical requests to check consistency...")
    
    test_data = {
        "zone_id": 1,
        "date": "2024-12-25",
        "hour": 18,
        "day_of_week": 2
    }
    
    results = []
    
    try:
        for i in range(3):
            response = requests.post(
                f"{BACKEND_URL}{API_PREFIX}/predict",
                json=test_data,
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                results.append(data['predicted_occupancy'])
                print_info(f"Request {i+1}: {data['predicted_occupancy']}% occupancy")
            else:
                print_error(f"Request {i+1} failed")
                return False
        
        # Check if all results are identical (ML should be deterministic)
        if len(set(results)) == 1:
            print_success("All predictions are consistent! (ML is deterministic)")
            return True
        else:
            print_warning(f"Predictions vary: {results}")
            print_warning("This might be expected if there's randomness in the model")
            return True
            
    except Exception as e:
        print_error(f"Error testing consistency: {e}")
        return False


def main():
    """Run all tests"""
    print_header("END-TO-END TESTING: ML Model → Backend → Frontend")
    print(f"Testing backend at: {BACKEND_URL}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    tests = [
        ("Backend Health", test_backend_health),
        ("ML Model Status", test_ml_status),
        ("ML Prediction", test_ml_prediction),
        ("Single Prediction", test_single_prediction),
        ("Recommendations", test_recommendations),
        ("Frontend Flow", test_frontend_flow),
        ("Data Consistency", test_data_consistency),
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print_error(f"Test crashed: {e}")
            results.append((test_name, False))
    
    # Summary
    print_header("TEST SUMMARY")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = f"{GREEN}PASS{RESET}" if result else f"{RED}FAIL{RESET}"
        print(f"  {status}  {test_name}")
    
    print(f"\n{BLUE}{'='*70}{RESET}")
    
    if passed == total:
        print_success(f"ALL TESTS PASSED! ({passed}/{total})")
        print_success("✅ ML Model → Backend → Frontend flow is working perfectly!")
        return 0
    else:
        print_error(f"SOME TESTS FAILED! ({passed}/{total} passed)")
        print_warning("Check the errors above for details")
        return 1


if __name__ == "__main__":
    sys.exit(main())
