from typing import Annotated
from fastapi import APIRouter, Depends, Query, Response

from api.dependencies import symptom_service
from services import SymptomService
from schemas import SymptomSchema, SymptomSchemaAdd

from auth.users import  current_active_user
from auth.db import User

router = APIRouter(
    prefix="/symptom",
    tags=["Symptom"],
)

@router.get("/get_all")
async def get_all(
    symptom_service: Annotated[SymptomService, Depends(symptom_service)],
    response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
    user: User = Depends(current_active_user)
):
    if user.is_doctor or user.is_superuser:
        symptoms = await symptom_service.get_all_symptoms()
        response.headers["X-Total-Count"] = str(len(symptoms))

        if _limit != 0:
            start = (_page - 1) * _limit
            end = start + _limit

            return symptoms[start:end]
        return symptoms
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.put("/update_one")
async def update_one_symptom(
    upd_symptom: SymptomSchema,
    symptom_service: Annotated[SymptomService, Depends(symptom_service)],
    user: User = Depends(current_active_user)
):
    if user.is_superuser:
        symptom = await symptom_service.update_symptom(upd_symptom)
        return symptom
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.post("/add_new")
async def add_symptom(
    new_symptom: SymptomSchemaAdd,
    symptom_service: Annotated[SymptomService, Depends(symptom_service)],
    user: User = Depends(current_active_user)
):
    if user.is_superuser:
        symptom = await symptom_service.add_new_symptom(new_symptom)
        return symptom
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )