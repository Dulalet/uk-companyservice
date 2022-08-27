from typing import Union
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate, CompanyUpdateRestricted


class CRUDCompany(CRUDBase[Company, CompanyCreate, CompanyUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Company,
        obj_in: Union[CompanyUpdate, CompanyUpdateRestricted]
    ) -> Company:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


company = CRUDCompany(Company)
