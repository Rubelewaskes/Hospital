from typing import Annotated
from fastapi import APIRouter, Depends, Query, Response

from api.dependencies import diagnosis_service
from schemas import DiagnosisSchema, DiagnosisSchemaAdd
from services.diagnosis import DiagnosisService

from auth.users import  current_active_user
from auth.db import User


router = APIRouter(
    prefix="/diagnosis",
    tags=["Diagnosis"],
)

@router.get("/get_all")
async def get_all_diagnosis(
    diagnosis_service: Annotated[DiagnosisService, Depends(diagnosis_service)],
    response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
    user: User = Depends(current_active_user),
):
    if user.is_doctor or user.is_superuser:
        diagnoses = await diagnosis_service.get_all_diagnosis()
        response.headers["X-Total-Count"] = str(len(diagnoses))

        if _limit != 0:
            start = (_page - 1) * _limit
            end = start + _limit

            return diagnoses[start:end]
        return diagnoses

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.put("/update_one")
async def update_one_diagnosis(
    upd_diagnosis: DiagnosisSchema,
    diagnosis_service: Annotated[DiagnosisService, Depends(diagnosis_service)],
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        diagnosis = await diagnosis_service.update_diagnosis(upd_diagnosis)
        return diagnosis

    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )

@router.post("/add_new")
async def add_new_diagnosis(
    diagnosis: DiagnosisSchemaAdd, 
    diagnosis_service: Annotated[DiagnosisService, Depends(diagnosis_service)],
    user: User = Depends(current_active_user),
):
    if user.is_superuser:
        added_diagnosis = await diagnosis_service.add_one_diagnosis(diagnosis)
        return added_diagnosis
        
    raise HTTPException(
            status_code=403,
            detail="Forbidden"
        )