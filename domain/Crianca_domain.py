from dataclasses import dataclass, field
import uuid



@dataclass
class Crianca:
    nome:str
    idade:int
    responsavel:str
    atrasos:int = 0
    bloqueada:bool=False
    id:str=field(default_factory=lambda:str(uuid.uuid4()))

    def __post_init__(self):
        self.validate()

    def validate(self):
        if self.idade<=0 or not self.idade:
            raise ValueError("Idade deve ser informada e deve ser maior que zero")
        if not self.responsavel or self.responsavel.strip()=="":
            raise ValueError("É necessário informar um responsável")
        if not self.nome or self.nome.strip()=="":
            raise ValueError("Nome é obrigatório")
        
    def validar_limite_atraso(self):
        if self.atrasos>=3 or self.bloqueada:
            raise ValueError(f"Criança {self.nome} com 3+ atrasos acumulados. Bloqueada para novos empréstimos")
                

    