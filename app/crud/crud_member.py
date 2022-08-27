from typing import Union
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.member import Member
from app.schemas.member import MemberCreate, MemberUpdate, MemberUpdateRestricted


class CRUDMember(CRUDBase[Member, MemberCreate, MemberUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Member,
        obj_in: Union[MemberUpdate, MemberUpdateRestricted]
    ) -> Member:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


member = CRUDMember(Member)
