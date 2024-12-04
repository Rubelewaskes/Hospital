from typing import Annotated
from fastapi import APIRouter, Depends

from api.dependencies import symptom_service
from services import SymptomService
from schemas import SymptomSchemaAdd

router = APIRouter(
    prefix="/symptom",
    tags=["Symptom"],
)

@router.get("/get_symptoms")
async def get_all_symptoms(
    symptom_service: Annotated[SymptomService, Depends(symptom_service)],
):
    symptoms = await symptom_service.get_all_symptoms()
    return symptoms

@router.post("/add_new")
async def add_symptom(
    new_symptom: SymptomSchemaAdd,
    symptom_service: Annotated[SymptomService, Depends(symptom_service)],
):
    symptom = await symptom_service.add_new_symptom(new_symptom)
    return symptom