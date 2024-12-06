from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Query, Response
from schemas.patient import PatientSchemaAdd, PatientSchemaUpd

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
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
):
    patients = await patient_service.get_all_patients()
    response.headers["X-Total-Count"] = str(len(patients))

    if _limit != 0:
        start = (_page - 1) * _limit
        end = start + _limit

        return patients[start:end]
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
    response: Response,
    _limit: int = Query(0, ge=0),
    _page: int = Query(1, ge=1),
):
    patients = await patient_service.get_all_patients_on_doctor_area(doctor_id)
    response.headers["X-Total-Count"] = str(len(patients))

    if _limit != 0:
        start = (_page - 1) * _limit
        end = start + _limit

        return patients[start:end]
    return patients

@router.put("/update")
async def update_patient(
    upd_patient: PatientSchemaUpd,
    patient_service: Annotated[PatientService, Depends(patient_service)],
):
    patient = await patient_service.update_patient(upd_patient)
    return patient

@router.post("/add_new")
async def add_new_patient(
    patient_data: PatientSchemaAdd,
    patient_service: Annotated[PatientService, Depends(patient_service)],
):
    added_data = await patient_service.add_new_patient(patient_data)
    return added_data