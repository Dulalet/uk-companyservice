from pydantic import BaseModel

from typing import Sequence


class DepartmentBase(BaseModel):
    company_id: int
    name_ru: str
    name_kz: str
    code: str


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(DepartmentBase):
    id: int


class DepartmentUpdateRestricted(DepartmentBase):
    id: int


# Properties shared by models stored in DB
class DepartmentInDBBase(DepartmentBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Department(DepartmentInDBBase):
    pass


# Properties properties stored in DB
class DepartmentInDB(DepartmentInDBBase):
    pass


class DepartmentSearchResults(BaseModel):
    results: Sequence[Department]
