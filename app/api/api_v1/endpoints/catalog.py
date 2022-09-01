import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from psycopg2 import errors

from app import crud
from app.api import deps
from app.schemas.catalog import Catalog, CatalogCreate, CatalogUpdate

router = APIRouter()

logger = logging.getLogger('')


@router.get("/{catalog_id}", status_code=200, response_model=Catalog)
def fetch_catalog(
    *,
    catalog_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    result = crud.catalog.get(db=db, id=catalog_id)
    if not result:
        raise HTTPException(
            status_code=400, detail=f"Catalog with ID {catalog_id} not found"
        )
    return result


@router.post("/", status_code=201, response_model=Catalog)
def create_catalog(
    *,
    catalog_in: CatalogCreate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Create a new catalog in the database.
    """
    try:
        catalog = crud.catalog.create(db=db, obj_in=catalog_in)
    except IntegrityError as e:
        try:
            raise e.orig
        except errors.UniqueViolation:
            raise HTTPException(
                status_code=400, detail=f"Catalog already exists"
            )
        except errors.ForeignKeyViolation:
            raise HTTPException(
                status_code=400, detail=f"No such department"
            )
    return catalog


@router.delete("/{catalog_id}", status_code=200)
def delete_catalog(
    *,
    catalog_id: int,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Delete Catalog
    """
    try:
        catalog = crud.catalog.remove(db=db, id=catalog_id)
    except SQLAlchemyError:
        raise HTTPException(
            status_code=400, detail=f"Could not delete"
        )
    return {"status": "success"}


@router.get("/", status_code=200, response_model=List[Catalog])
def list_catalog(
    *, db: Session = Depends(deps.get_db)
) -> list:
    """
    Получить список всех касс, где user_id is Catalog
    """
    catalogs = crud.catalog.get_multi(db=db, limit=10)
    return catalogs


@router.patch("/", status_code=201, response_model=Catalog)
def update_catalog(
    *,
    catalog_in: CatalogUpdate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Update catalog in the database.
    """
    try:
        catalog = crud.catalog.get(db, id=catalog_in.id)
    except Exception as e:
        logger.error(e)
    if not catalog:
        raise HTTPException(
            status_code=400, detail=f"Catalog with ID: {catalog_in.id} not found."
        )
    try:
        updated_catalog = crud.catalog.update(
            db=db, db_obj=catalog, obj_in=catalog_in)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail=f"Can not update"
        )
    return updated_catalog
