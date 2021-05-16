# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User # noqa
from app.models.pet import Pet #noqa
from app.models.pettype import PetType #noqa