from pydantic import BaseModel

from typing import Sequence


class CompanyMemberBase(BaseModel):
    company_id: int
    member_id: int
    type: str


class CompanyMemberCreate(CompanyMemberBase):
    pass


class CompanyMemberUpdate(CompanyMemberBase):
    id: int


class CompanyMemberUpdateRestricted(CompanyMemberBase):
    id: int


# Properties shared by models stored in DB
class CompanyMemberInDBBase(CompanyMemberBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class CompanyMember(CompanyMemberInDBBase):
    pass


# Properties properties stored in DB
class CompanyMemberInDB(CompanyMemberInDBBase):
    pass


class CompanyMemberSearchResults(BaseModel):
    results: Sequence[CompanyMember]
