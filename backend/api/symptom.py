from typing import Annotated
from fastapi import APIRouter, Depends, Query, Response

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
    response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
):
    symptoms = await symptom_service.get_all_symptoms()
    response.headers["X-Total-Count"] = str(len(symptoms))

    if _limit != 0:
        start = (_page - 1) * _limit
        end = start + _limit

        return symptoms[start:end]
    return symptoms

@router.post("/add_new")
async def add_symptom(
    new_symptom: SymptomSchemaAdd,
    symptom_service: Annotated[SymptomService, Depends(symptom_service)],
):
    symptom = await symptom_service.add_new_symptom(new_symptom)
    return symptom