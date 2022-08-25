from app.crud.base import CRUDBase
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


class CRUDRecipe(CRUDBase[Company, CompanyCreate, CompanyUpdate]):
    ...


company = CRUDRecipe(Company)