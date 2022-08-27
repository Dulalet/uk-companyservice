# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.company import Company, CompanyMember  # noqa
from app.models.member import Member  # noqa
from app.models.department import Department  # noqa
from app.models.catalog import Catalog  # noqa
