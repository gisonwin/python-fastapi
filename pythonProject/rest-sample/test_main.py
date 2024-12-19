from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine

from .main import app, get_session


def test_create_hero():
    client = TestClient(app)
    response = client.post('/heroes/', json={"name": "Deadpond1", "secret_name": "Deadpond1 Wilson"})

    json_data = response.json()
    assert response.status_code == 200
    assert json_data['name'] == 'Deadpond1'
    assert json_data['secret_name'] == 'Deadpond1 Wilson'
    assert json_data['age'] is None
    assert json_data['id'] is not None
