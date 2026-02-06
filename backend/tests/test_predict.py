"""Tests for prediction endpoints."""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_predict_endpoint():
    """Test prediction endpoint."""
    response = client.post(
        "/api/v1/predict",
        json={
            "zone_id": 1,
            "day_of_week": 1,
            "hour": 14,
            "date": "2026-02-07"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "availability_level" in data
    assert "confidence_score" in data
    assert data["availability_level"] in ["High", "Medium", "Low"]


def test_predict_invalid_zone():
    """Test prediction with invalid zone."""
    response = client.post(
        "/api/v1/predict",
        json={
            "zone_id": 999,
            "day_of_week": 1,
            "hour": 14,
            "date": "2026-02-07"
        }
    )
    assert response.status_code == 404
