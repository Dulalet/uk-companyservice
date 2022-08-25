from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional

from app import crud
from app.api import deps
from app.schemas.company import Company, CompanyCreate, CompanySearchResults

router = APIRouter()


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