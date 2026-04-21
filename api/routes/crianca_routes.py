from fastapi import APIRouter, HTTPException
from domain.Crianca_domain import Crianca
from schemas.crianca_schema import CriancaCreate, CriancaOut
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
    return list_criancas()

