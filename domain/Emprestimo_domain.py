from pydantic import BaseModel
from datetime import date
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
    data_retirado:date
    data_entregue:date
    status:str
    multa:float
    atrasos:int = 0
    id:str=field(default_factory=lambda:str(uuid.uuid4()))

    def calcular_multa(self):
        delta = self.data_entregue-self.data_retirado
        dias_totais = delta.days
        if (dias_totais)>7:
            dias_atraso = dias_totais-7
            self.multa = float(dias_atraso*2)
            self.atrasos+=1
            return self.multa
        self.multa=0.0
        return self.multa
    
    
    

    

