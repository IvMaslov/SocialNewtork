from fastapi.testclient import TestClient
from ..main import app

client  = TestClient(app)

def test_signup_wrong_email():
    response = client.post("/signup", json={"email": "wrong", "password": "qwerty"})
    assert response.status_code == 400

    response = client.post("/signup", json={"email": 2, "password": "qwerty"})
    assert response.status_code == 422