from uuid import UUID
from pydantic import BaseModel

from typing import Optional, Sequence


class MemberBase(BaseModel):
    user_uuid: UUID


class MemberCreate(MemberBase):
    pass


class MemberUpdate(MemberBase):
    id: int


class MemberUpdateRestricted(MemberBase):
    id: int


# Properties shared by models stored in DB
class MemberInDBBase(MemberBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Member(MemberInDBBase):
    pass


# Properties properties stored in DB
class MemberInDB(MemberInDBBase):
    pass


class MemberSearchResults(BaseModel):
    results: Sequence[Member]
