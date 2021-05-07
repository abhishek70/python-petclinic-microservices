from fastapi.testclient import TestClient
from ....core.config import settings


def test_health(
        client: TestClient
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/actuators/health"
    )
    assert response.status_code == 200
    assert response.json() == {"status": "up"}
