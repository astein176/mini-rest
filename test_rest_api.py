from fastapi.testclient import TestClient
from rest_api import app

client = TestClient(app)

VALID_BLIP = {
  "flight_id": "FIRE",
  "latitude": -90,
  "longitude": -180,
  "altitude": 100000,
  "timestamp": "2026-10-26T16:53:51.824000Z"
}


def test_create_blip():
    response = client.post("/v0/blips", json=VALID_BLIP)

    assert response.status_code == 201
    assert "flight_id" in response.json()


def test_get_blip():
    # First, create a blip to ensure there is one to retrieve
    response = client.post("/v0/blips", json=VALID_BLIP)
    blip_id = response.json()["id"]

    response = client.get(f"/v0/blips/{blip_id}")

    assert response.status_code == 200
    body = response.json()
    assert body["flight_id"] == VALID_BLIP["flight_id"]
    assert body["latitude"] == VALID_BLIP["latitude"]
    assert body["longitude"] == VALID_BLIP["longitude"]
    assert body["altitude"] == VALID_BLIP["altitude"]


def test_invalid_latitude():
    invalid_blip = VALID_BLIP.copy()
    invalid_blip["latitude"] = 400  # Invalid latitude

    response = client.post("/v0/blips", json=invalid_blip)

    assert response.status_code == 422  # Unprocessable Entity


def test_missing_field():
    invalid_blip = VALID_BLIP.copy()
    del invalid_blip["flight_id"]  # Remove required field

    response = client.post("/v0/blips", json=invalid_blip)

    assert response.status_code == 422  # Unprocessable Entity


def test_get_blip_not_found():
    response = client.get("/v0/blips/2147483647")

    assert response.status_code == 404
    assert response.json() == {"detail": "Blip not found"}


def test_get_blip_id_out_of_range():
    response = client.get("/v0/blips/2147483648")

    assert response.status_code == 422