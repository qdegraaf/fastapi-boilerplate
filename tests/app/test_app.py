from starlette.testclient import TestClient

from app.app import app

client = TestClient(app)


def test_health_check():
    response = client.get("/")

    assert response.status_code == 200
    assert response.content == b'{"Status":"Healthy as a fish"}'
