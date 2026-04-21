from dataclasses import dataclass, field
import uuid



@dataclass(frozen=True)
class Crianca:
    nome:str
    idade:int
    responsavel:str
    id:str=field(default_factory=lambda:str(uuid.uuid4()))

    def __post_init__(self):
        self.validate()

    def validate(self):
        if self.idade<=0 or not idade:
            raise ValueError("Idade deve ser informada e deve ser maior que zero")
        if not self.responsavel or self.responsavel.strip()=="":
            raise ValueError("É necessário informar um responsável")
        if not self.nome or self.nome.strip()=="":
            raise ValueError("Nome é obrigatório")
        

    