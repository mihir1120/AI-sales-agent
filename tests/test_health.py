from fastapi.testclient import TestClient

from apps.api.app.main import app


def test_health_endpoint_returns_service_status():
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "Sales AI Agent API"}
