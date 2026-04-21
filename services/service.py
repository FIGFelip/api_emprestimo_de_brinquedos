from domain.Crianca_domain import Crianca
from domain.Brinquedo_domain import Brinquedo
from domain.Emprestimo_domain import Emprestimo, multa_input, devolucao_input
from repositories.memory import db


def create_crianca(data)->Crianca:
    crianca = Crianca(
        nome=data.nome,
        idade=data.idade,
        responsavel=data.responsavel
    )
    db.criancas[crianca.id]=crianca
    return crianca

def list_criancas()->list[Crianca]:
    return list(db.criancas.values())


def create_brinquedo(data)->Brinquedo:
    brinquedo = Brinquedo(
        nome=data.nome,
        categoria=data.categoria,
        faixa_etaria_minima=data.faixa_etaria_minima,
        disponivel=data.disponivel
    )
    db.brinquedos[brinquedo.id]=brinquedo
    return brinquedo

def list_brinquedos()->list[Brinquedo]:
    return list(db.brinquedos.values())

def create_emprestimo(data)->Emprestimo:
    emprestimo = Emprestimo(
        crianca_id=data.crianca_id,
        brinquedo_id=data.brinquedo_id,
        datas=data.datas,
        status=data.status,
        multa=data.multa
    )
    db.emprestimos[emprestimo.id]=emprestimo
    return emprestimo

def list_emprestimos()->list[Emprestimo]:
    return list(db.emprestimos.values())

def buscar_emprestimo(id:str)->Emprestimo:
    return db.emprestimos.get(id)

def devolver(id:str)->Emprestimo:
    emprestimo = db.emprestimos.get(id)
    if not emprestimo:
        raise ValueError("Empréstimo não encontrado")
    emprestimo.status="devolvido"
    return emprestimo

def get_crianca_emprestimo(id):
    crianca = db.criancas.get(id)
    if not crianca:
        raise ValueError("Criança não encontrada")
    return list(db.emprestimos.get(id))
    