from dataclasses import dataclass, field
from domain.Crianca_domain import Crianca
import uuid
@dataclass
class Brinquedo:
    nome:str
    categoria:str
    faixa_etaria_minima:int
    disponivel:bool = True
    id:str=field(default_factory=lambda:str(uuid.uuid4()))


    def emprestar(self):
        if not self.disponivel:
            raise ValueError("brinquedo indisponivel")
        self.disponivel=False
    
    
    
    