from typing import Union
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.department import Department
from app.schemas.department import DepartmentCreate, DepartmentUpdate, DepartmentUpdateRestricted


class CRUDDepartment(CRUDBase[Department, DepartmentCreate, DepartmentUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Department,
        obj_in: Union[DepartmentUpdate, DepartmentUpdateRestricted]
    ) -> Department:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


department = CRUDDepartment(Department)
