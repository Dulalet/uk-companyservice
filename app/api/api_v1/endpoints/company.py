import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app import crud
from app.api import deps
from app.schemas.company import Company, CompanyCreate, CompanyUpdate, UserIn
from app.schemas.companymember import CompanyMemberCreate

router = APIRouter()

logger = logging.getLogger('')


@router.get("/{company_id}", status_code=200, response_model=Company)
def fetch_company(
    *,
    company_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    result = crud.company.get(db=db, id=company_id)
    if not result:
        raise HTTPException(
            status_code=400, detail=f"Company with ID {company_id} not found"
        )
    return result


@router.post("/", status_code=201, response_model=Company)
def create_company(
    *,
    company_in: CompanyCreate,
    user: UserIn,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Create a new company in the database.
    """
    try:
        company = crud.company.create(db=db, obj_in=company_in)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail=f"Company already exists."
        )
    try:
        member = crud.member.create(db=db, obj_in=user)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail=f"Member already exists."
        )
    companymember = CompanyMemberCreate(
        company_id=company.id,
        member_id=member.id,
        type='owner')
    crud.companymember.create(db=db, obj_in=companymember)
    return company


@router.delete("/{company_id}", status_code=200)
def delete_company(
    *,
    company_id: int,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Delete Company
    """
    try:
        company = crud.company.remove(db=db, id=company_id)
    except SQLAlchemyError:
        raise HTTPException(
            status_code=400, detail=f"Could not delete"
        )
    return {"status": "success"}


@router.get("/", status_code=200, response_model=List[Company])
def list_companies(
    *, db: Session = Depends(deps.get_db)
) -> list:
    """
    Получить список всех касс, где user_id is Member
    """
    companies = crud.company.get_multi(db=db, limit=10)
    return companies


@router.put("/", status_code=201, response_model=Company)
def update_company(
    *,
    company_in: CompanyUpdate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Update company in the database.
    """
    try:
        company = crud.company.get(db, id=company_in.id)
    except Exception as e:
        logger.error(e)
    if not company:
        raise HTTPException(
            status_code=400, detail=f"Recipe with ID: {company_in.id} not found."
        )
    try:
        updated_company = crud.company.update(
            db=db, db_obj=company, obj_in=company_in)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail=f"Can't update: company with given bin_iin exists"
        )
    return updated_company
