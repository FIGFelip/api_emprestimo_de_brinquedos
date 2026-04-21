from fastapi import APIRouter, HTTPException
from schemas.emprestimo_schema import EmprestimoCreate, EmprestimoOut
from services.service import (
    create_emprestimo,
    list_emprestimos,
    buscar_emprestimo,
    devolver,
    get_crianca_emprestimo
)

router = APIRouter(prefix="/emprestimos", tags=["emprestimos"])

@router.post("/", response_model=EmprestimoOut)
def post_emprestimo(data:EmprestimoCreate):
    return create_emprestimo(data)


@router.get("/", response_model=list[EmprestimoOut])
def get_emprestimos():
    return list_emprestimos()



@router.get("/{id}", response_model=EmprestimoOut)
def get_emprestimo(id):
    return buscar_emprestimo(id)

