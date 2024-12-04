from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import diagnosis_service
from schemas import DiagnosisSchemaAdd
from services.diagnosis import DiagnosisService

router = APIRouter(
    prefix="/diagnosis",
    tags=["Diagnosis"],
)

@router.post("/add_new")
async def add_new_diagnosis(
    diagnosis: DiagnosisSchemaAdd, 
    diagnosis_service: Annotated[DiagnosisService, Depends(diagnosis_service)],
):
    added_diagnosis = await diagnosis_service.add_one_diagnosis(diagnosis)
    return added_diagnosis