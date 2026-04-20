from fastapi import APIRouter, HTTPException
from domain.CriancaDomain import Crianca
from schemas.CriancaSchema import CriancaCreate, CriancaOut
from services.service import (
    create_crianca,
    list_criancas
)
router = APIRouter(prefix="/criancas", tags=["criancas"])

@router.post("/", response_model=CriancaOut)
def post_crianca(data:CriancaCreate):
    return create_crianca(data)


@router.get("/",response_model=list[CriancaOut])
def get_criancas():
    return get_criancas()

