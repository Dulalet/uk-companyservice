import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app import crud
from app.api import deps
from app.schemas.department import Department, DepartmentCreate, DepartmentUpdate

router = APIRouter()

logger = logging.getLogger('')


@router.get("/{department_id}", status_code=200, response_model=Department)
def fetch_department(
    *,
    department_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    result = crud.department.get(db=db, id=department_id)
    if not result:
        raise HTTPException(
            status_code=400, detail=f"Department with ID {department_id} not found"
        )
    return result


@router.post("/", status_code=201, response_model=Department)
def create_department(
    *,
    department_in: DepartmentCreate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Create a new department in the database.
    """
    try:
        department = crud.department.create(db=db, obj_in=department_in)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail=f"Department already exists"
        )
    return department


@router.delete("/{department_id}", status_code=200)
def delete_department(
    *,
    department_id: int,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Delete Department
    """
    try:
        department = crud.department.remove(db=db, id=department_id)
    except SQLAlchemyError:
        raise HTTPException(
            status_code=400, detail=f"Could not delete"
        )
    return {"status": "success"}


@router.get("/", status_code=200, response_model=List[Department])
def list_departments(
    *, db: Session = Depends(deps.get_db)
) -> list:
    """
    Получить список всех касс, где user_id is Department
    """
    departments = crud.department.get_multi(db=db, limit=10)
    return departments


@router.patch("/", status_code=201, response_model=Department)
def update_department(
    *,
    department_in: DepartmentUpdate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Update department in the database.
    """
    try:
        department = crud.department.get(db, id=department_in.id)
    except Exception as e:
        logger.error(e)
    if not department:
        raise HTTPException(
            status_code=400, detail=f"Department with ID: {department_in.id} not found."
        )
    try:
        updated_department = crud.department.update(
            db=db, db_obj=department, obj_in=department_in)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail=f"Can not update"
        )
    return updated_department
