from domain.Crianca_domain import Crianca
from domain.Brinquedo_domain import Brinquedo
from schemas.emprestimo_schema import EmprestimoCreate
from schemas.brinquedo_schema import BrinquedoCreate
from schemas.crianca_schema import CriancaCreate
from domain.Emprestimo_domain import Emprestimo
from fastapi import HTTPException
from datetime import timedelta
from repositories.memory import db


def create_crianca(data:CriancaCreate)->Crianca:
    crianca = Crianca(
        nome=data.nome,
        idade=data.idade,
        responsavel=data.responsavel
    )
    db.criancas_por_id[crianca.id]=crianca
    return crianca

def list_criancas()->list[Crianca]:
    return list(db.criancas_por_id.values())


def create_brinquedo(data:BrinquedoCreate)->Brinquedo:
    brinquedo = Brinquedo(
        nome=data.nome,
        categoria=data.categoria,
        faixa_etaria_minima=data.faixa_etaria_minima,
        disponivel=data.disponivel
    )
    db.brinquedos_por_id[brinquedo.id]=brinquedo
    return brinquedo

def list_brinquedos()->list[Brinquedo]:
    return list(db.brinquedos_por_id.values())

def create_emprestimo(data:EmprestimoCreate)->Emprestimo:
    
    crianca = db.criancas_por_id.get(data.crianca_id)
    
    brinquedo= db.brinquedos_por_id.get(data.brinquedo_id)

    if not crianca or not brinquedo:
        raise HTTPException(status_code=404, detail="Criança ou brinquedo não encontrados")
    
    crianca.validar_limite_atraso()
    brinquedo.emprestar
    
    
    emprestimo = Emprestimo(
        crianca_id=data.crianca_id,
        brinquedo_id=data.brinquedo_id,
        data_retirado=data.data_retirado,
        data_entregue=data.data_retirado + timedelta(days=7),
        status="ativo",
        multa=0.0
    )
    db.emprestimos_por_id[emprestimo.id]=emprestimo
    return emprestimo



def list_emprestimos()->list[Emprestimo]:
    return list(db.emprestimos_por_id.values())

def buscar_emprestimo(id:str)->Emprestimo:
    return db.emprestimos_por_id.get(id)

def devolver(id:str)->Emprestimo:
    emprestimo = db.emprestimos_por_id.get(id)
    if not emprestimo:
        raise ValueError("Empréstimo não encontrado")
    emprestimo.status="devolvido"
    return emprestimo

def get_crianca_emprestimo(id):
    crianca = db.criancas_por_id.get(id)
    if not crianca:
        raise ValueError("Criança não encontrada")
    return list(db.emprestimos_por_id.get(id))
    