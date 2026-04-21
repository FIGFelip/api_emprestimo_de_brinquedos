from fastapi import APIRouter, HTTPException
from schemas.brinquedo_schema import BrinquedoCreate, BrinquedoOut
from services.service import (
    create_brinquedo,
    list_brinquedos
)

router = APIRouter(prefix="/brinquedos", tags=["brinquedos"])

@router.post("/", response_model=BrinquedoOut)
def post_brinquedo(data:BrinquedoCreate):
    return create_brinquedo(data)


@router.get("/", response_model=list[BrinquedoOut])
def get_brinquedos():
    return list_brinquedos()

