from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from ....core.config import settings
from ...utils.utils import random_datetime, random_integer, random_lower_string
from ...utils.visit import create_random_pet_visits


def test_read_visit(client: TestClient, db: Session) -> None:
    pet_id = random_integer()
    visit = create_random_pet_visits(db, pet_id)
    visit2 = create_random_pet_visits(db, pet_id)
    response = client.get(f"{settings.API_V1_STR}/pets/{pet_id}/visits", headers="")
    assert response.status_code == 200
    content = response.json()
    assert len(content) == 2
