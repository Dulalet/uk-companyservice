from pydantic import BaseModel

from typing import Optional, Sequence

from app.api.api_v1.endpoints import department


class CatalogBase(BaseModel):
    department_id: int
    code: Optional[str]
    code_hatch: Optional[str]
    name_ru: str
    name_kz: str
    pay_nds: bool = False
    price: float = 0
    quantity_type: int = 796


class CatalogCreate(CatalogBase):
    pass


class CatalogUpdate(CatalogBase):
    id: int


class CatalogUpdateRestricted(CatalogBase):
    id: int


# Properties shared by models stored in DB
class CatalogInDBBase(CatalogBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Catalog(CatalogInDBBase):
    pass


# Properties properties stored in DB
class CatalogInDB(CatalogInDBBase):
    pass


class CatalogSearchResults(BaseModel):
    results: Sequence[Catalog]
