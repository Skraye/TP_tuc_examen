import json
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_items(mocker):
    """
        validate if the items are returned
    """
    response_data = [
        {"name":"","description":"","id":0,"trainer_id":0},
        {"name":"","description":"","id":2,"trainer_id":0},
        {"name":"","description":"","id":1,"trainer_id":0},
        {"name":"","description":"","id":3,"trainer_id":1}
        ]
    mocker.patch(
    "app.actions.get_items",
    return_value= response_data
    )
    response = client.get("/items/?skip=0&limit=100")
    assert response.status_code == 200
    assert response.json() == response_data
