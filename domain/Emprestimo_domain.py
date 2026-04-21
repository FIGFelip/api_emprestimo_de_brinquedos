from pydantic import BaseModel
from dataclasses import dataclass, field
import uuid

class multa_input(BaseModel):
    valor_multa:float

class devolucao_input(BaseModel):
    id_emprestimo:str

@dataclass
class Emprestimo:
    crianca_id:str
    brinquedo_id:str
    data_entrada:int
    data_saida:int
    status:str
    multa:float
    id:str=field(default_factory=lambda:str(uuid.uuid4()))

    def calcular_multa(self):
        dias_emprestado = self.data_entrada-self.data_saida
        atrasos=0
        if (dias_emprestado)>7:
            multa = (dias_emprestado*2)
            atrasos+=1
            return multa
        return {"Dentro do limite, sem multa aplicada"}

    def bloquear_crianca(self):
        if self.atrasos>=3:
            return {"3 atrasos registrados. criança bloqueada"}
    
    

    

