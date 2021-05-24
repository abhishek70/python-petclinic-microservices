from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.utils import random_integer, create_random_pettype, random_pet_type


def test_read_pet_types(client: TestClient, db: Session) -> None:
    response = client.get(f"{settings.API_V1_STR}/pettypes/", headers="")
    assert response.status_code == 200


def test_read_pet_type(client: TestClient, db: Session) -> None:
    pet_type = create_random_pettype(db)
    response = client.get(f"{settings.API_V1_STR}/pettypes/{pet_type.id}", headers="")
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == pet_type.name
    assert content["id"] == pet_type.id


def test_create_pet_type(client: TestClient, db: Session) -> None:
    data = {
        "name": f"{random_pet_type()}"
    }
    response = client.post(f"{settings.API_V1_STR}/pettypes/", headers="", json=data)
    assert response.status_code == 201
    content = response.json()
    assert content["name"] == data["name"]
    assert "id" in content
