"""Tests for zone endpoints."""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_zones():
    """Test getting all zones."""
    response = client.get("/api/v1/zones")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_zone_by_id():
    """Test getting a specific zone."""
    response = client.get("/api/v1/zones/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert data["id"] == 1
