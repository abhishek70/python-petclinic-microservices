from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from ....core.config import settings
from ...utils.utils import random_datetime, random_integer, random_lower_string
from ...utils.visit import create_random_visit


def test_read_visit(client: TestClient, db: Session) -> None:
    visit = create_random_visit(db)
    response = client.get(f"{settings.API_V1_STR}/visits/{visit.id}", headers="")
    assert response.status_code == 200
    content = response.json()
    assert content["pet_id"] == visit.pet_id
    assert content["id"] == visit.id


def test_create_visit(client: TestClient, db: Session) -> None:
    data = {
        "description": f"{random_lower_string()}",
        "visit_date": f"{random_datetime()}",
        "pet_id": random_integer(),
    }
    response = client.post(f"{settings.API_V1_STR}/visits/", headers="", json=data)
    assert response.status_code == 201
    content = response.json()
    assert content["pet_id"] == data["pet_id"]
    assert content["description"] == data["description"]
    assert "pet_id" in content
    assert "visit_date" in content


def test_update_visit(client: TestClient, db: Session) -> None:
    visit = create_random_visit(db)
    data = {
        "description": f"{random_lower_string()}",
        "visit_date": f"{random_datetime()}",
    }
    response = client.put(
        f"{settings.API_V1_STR}/visits/{visit.id}", headers="", json=data
    )
    assert response.status_code == 200
    content = response.json()
    assert data["description"] == content["description"]


def test_delete_visit(client: TestClient, db: Session) -> None:
    visit = create_random_visit(db)
    response = client.delete(f"{settings.API_V1_STR}/visits/{visit.id}", headers="")
    assert response.status_code == 200
