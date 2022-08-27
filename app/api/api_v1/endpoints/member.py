import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any, List
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app import crud
from app.api import deps
from app.schemas.member import Member, MemberCreate, MemberUpdate

router = APIRouter()

logger = logging.getLogger('')


@router.get("/{member_id}", status_code=200, response_model=Member)
def fetch_member(
    *,
    member_id: int,
    db: Session = Depends(deps.get_db)
) -> Any:
    result = crud.member.get(db=db, id=member_id)
    if not result:
        raise HTTPException(
            status_code=400, detail=f"Member with ID {member_id} not found"
        )
    return result


@router.post("/", status_code=201, response_model=Member)
def create_member(
    *,
    member_in: MemberCreate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Create a new member in the database.
    """
    try:
        member = crud.member.create(db=db, obj_in=member_in)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail=f"Member already exists"
        )
    return member


@router.delete("/{member_id}", status_code=200)
def delete_member(
    *,
    member_id: int,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Delete Member
    """
    try:
        member = crud.member.remove(db=db, id=member_id)
    except SQLAlchemyError:
        raise HTTPException(
            status_code=400, detail=f"Could not delete"
        )
    return {"status": "success"}


@router.get("/", status_code=200, response_model=List[Member])
def list_members(
    *, db: Session = Depends(deps.get_db)
) -> list:
    """
    Получить список всех касс, где user_id is Member
    """
    members = crud.member.get_multi(db=db, limit=10)
    return members


@router.put("/", status_code=201, response_model=Member)
def update_member(
    *,
    member_in: MemberUpdate,
    db: Session = Depends(deps.get_db),
) -> dict:
    """
    Update member in the database.
    """
    try:
        member = crud.member.get(db, id=member_in.id)
    except Exception as e:
        logger.error(e)
    if not member:
        raise HTTPException(
            status_code=400, detail=f"Member with ID: {member_in.id} not found."
        )
    try:
        updated_member = crud.member.update(
            db=db, db_obj=member, obj_in=member_in)
    except IntegrityError:
        raise HTTPException(
            status_code=400, detail=f"Can not update"
        )
    return updated_member
