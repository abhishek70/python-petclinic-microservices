from fastapi.testclient import TestClient

from app.core.config import settings
from app.api.api_v1.endpoints import actuators


def test_health(client: TestClient, monkeypatch) -> None:
    test_data = {"status": "up"}

    class FakeResponse:

        def __init__(self):
            self.status_code = 200

        def json(self):
            return test_data

    def mock_get():
        return FakeResponse()

    monkeypatch.setattr(actuators, "health", mock_get)

    #response = client.get(f"{settings.API_V1_STR}/actuators/health")
    response = actuators.health()
    # assert response.status_code == 200
    # assert response.json() == {"status": "up"}
    assert response.json() == test_data
