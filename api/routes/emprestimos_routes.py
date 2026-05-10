from fastapi import APIRouter, HTTPException
from schemas.emprestimo_schema import EmprestimoCreate, EmprestimoOut
from services.service import (
    create_emprestimo,
    list_emprestimos,
    buscar_emprestimo
)

router = APIRouter(prefix="/emprestimos", tags=["emprestimos"])

@router.post("/", response_model=EmprestimoOut)
def post_emprestimo(data:EmprestimoCreate):
    try:
        return create_emprestimo(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=list[EmprestimoOut])
def get_emprestimos():
    try:  
        return list_emprestimos()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{id}", response_model=EmprestimoOut)
def get_emprestimo(id):
    try:
        return buscar_emprestimo(id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
