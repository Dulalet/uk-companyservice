from unicodedata import name
from pydantic import BaseModel, HttpUrl

from typing import Sequence


class CompanyBase(BaseModel):
    bin_iin: str
    name: str
    address: str
    tax_mode: int


class CompanyCreate(CompanyBase):
    bin_iin: str
    name: str
    address: str
    tax_mode: int


class CompanyUpdate(CompanyBase):
    bin_iin: str
    name: str
    address: str
    tax_mode: int


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