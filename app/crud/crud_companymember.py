from typing import Union
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.company import CompanyMember
from app.schemas.companymember import CompanyMemberCreate, CompanyMemberUpdate, CompanyMemberUpdateRestricted


class CRUDCompanyMember(CRUDBase[CompanyMember, CompanyMemberCreate, CompanyMemberUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: CompanyMember,
        obj_in: Union[CompanyMemberUpdate, CompanyMemberUpdateRestricted]
    ) -> CompanyMember:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


companymember = CRUDCompanyMember(CompanyMember)
