from fastapi import APIRouter

from app.api.api_v1.endpoints import catalog, company, department, member


api_router = APIRouter()
api_router.include_router(company.router, prefix="/company", tags=["company"])
api_router.include_router(member.router, prefix="/member", tags=["member"])
api_router.include_router(
    department.router, prefix="/department", tags=["department"])
api_router.include_router(catalog.router, prefix="/catalog", tags=["catalog"])
