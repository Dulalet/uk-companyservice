from unicodedata import name
from pydantic import BaseModel, HttpUrl

from typing import List, Optional, Sequence


class UserIn(BaseModel):
    user_id: int


class CompanyBase(BaseModel):
    bin_iin: str
    name: str
    address: str
    tax_mode: Optional[int] = 3
    pay_nds: Optional[bool] = False
    seria_nds: Optional[str]
    number_nds: Optional[str]
    nds_type: Optional[int] = 0
    pin_prog: Optional[str]
    pin_kassa_in: Optional[str]
    pin_close_shift: Optional[str]
    pin_rmni: Optional[str]
    filled_fields: Optional[bool] = False


class CompanyCreate(CompanyBase):
    pass

class CompanyUpdate(CompanyBase):
    id: int


class CompanyUpdateRestricted(CompanyBase):
    id: int


# Properties shared by models stored in DB
class CompanyInDBBase(CompanyBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Company(CompanyInDBBase):
    pass


# Properties properties stored in DB
class CompanyInDB(CompanyInDBBase):
    pass


class CompanySearchResults(BaseModel):
    results: Sequence[Company]
