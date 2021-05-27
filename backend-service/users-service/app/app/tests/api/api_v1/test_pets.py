from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app import crud
from app.tests.utils.pet import create_random_pet
from app.tests.utils.pettype import create_random_pettype


def test_create_pet(
        client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    pettype = create_random_pettype(db)
    data = {"name": "Foo", "birth_date": "2020-10-11", "type_id": pettype.id}
    response = client.post(
        f"{settings.API_V1_STR}/pets/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 201
    content = response.json()
    assert content["name"] == data["name"]
    assert content["type_id"] == pettype.id
    assert "id" in content
    assert "owner_id" in content


def test_update_pet(
        client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    pet = create_random_pet(db)
    data = {"name": "Test"}
    response = client.put(
        f"{settings.API_V1_STR}/pets/{pet.id}", headers=superuser_token_headers, json=data
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] != pet.name
    assert content["name"] == data["name"]
    assert content["id"] == pet.id
    assert content["owner_id"] == pet.owner_id


def test_read_pet(
        client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    pet = create_random_pet(db)
    response = client.get(
        f"{settings.API_V1_STR}/pets/{pet.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["name"] == pet.name
    assert content["id"] == pet.id
    assert content["owner_id"] == pet.owner_id


def test_delete_pet(
        client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    pet = create_random_pet(db)
    response = client.delete(
        f"{settings.API_V1_STR}/pets/{pet.id}", headers=superuser_token_headers
    )
    assert response.status_code == 200
    pet = crud.pet.get(db=db, id=pet.id)
    assert pet is None
