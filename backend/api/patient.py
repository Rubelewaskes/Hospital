from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, Response
from schemas.patient import PatientSchemaAdd

from api.dependencies import patient_service
from services.patient import PatientService

router = APIRouter(
    prefix="/patient",
    tags=["Patient"],
)


@router.get("/get_all")
async def get_all_patients(
    patient_service: Annotated[PatientService, Depends(patient_service)],
    response: Response,
):
    patients = await patient_service.get_all_patients()
    response.headers["X-Total-Count"] = str(len(patients))

    return patients

@router.get("/get_one/{patient_id}")
async def get_one_patient(
    patient_id: int,
    patient_service: Annotated[PatientService, Depends(patient_service)],
):
    if patient := await patient_service.get_one_patient(patient_id):
        return patient
    raise HTTPException(
        status_code=404,
        detail="Patient not found"
    )

@router.get("/get_all_patients_of_doctor/{doctor_id}")
async def get_all_patients_of_doctor(
    doctor_id: int,
    patient_service: Annotated[PatientService, Depends(patient_service)],
):
    patients = await patient_service.get_all_patients_on_doctor_area(doctor_id)
    return patients

@router.post("/add_new")
async def add_new_patient(
    patient_data: PatientSchemaAdd,
    patient_service: Annotated[PatientService, Depends(patient_service)],
):
    added_data = await patient_service.add_new_patient(patient_data)
    return added_data