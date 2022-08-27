from typing import Union
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.catalog import Catalog
from app.schemas.catalog import CatalogCreate, CatalogUpdate, CatalogUpdateRestricted


class CRUDCatalog(CRUDBase[Catalog, CatalogCreate, CatalogUpdate]):
    def update(
        self,
        db: Session,
        *,
        db_obj: Catalog,
        obj_in: Union[CatalogUpdate, CatalogUpdateRestricted]
    ) -> Catalog:
        db_obj = super().update(db, db_obj=db_obj, obj_in=obj_in)
        return db_obj


catalog = CRUDCatalog(Catalog)
