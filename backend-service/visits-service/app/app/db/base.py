# Import all the models, so that Base has them before being
# imported by Alembic
from ..models.visit import Visit  # noqa
from .base_class import Base  # noqa
