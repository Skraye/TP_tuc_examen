"""Test trainers routes
    """
import json
from main import app
import requests
from fastapi.testclient import TestClient
client = TestClient(app)


def test_get_trainers():
    """
        get trainer
    """
    response = client.get("/trainers")
    assert response.status_code == 200


def test_post_api_trainers():
    """
        add one trainer with post
    """
    url = "http://localhost:8000/trainers/"
    headers = {'Content-Type': 'application/json'}
    info = {"name": "Rémi", "birthdate": "2001-04-24"}
    resp = requests.post(url, headers=headers,
                         data=json.dumps(info, indent=4), timeout=10)

    assert resp.status_code == 200
