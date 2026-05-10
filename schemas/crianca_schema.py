from pydantic import BaseModel

class CriancaCreate(BaseModel):
    nome:str
    idade:int
    responsavel:str
    atrasos:int=0
    bloqueada:bool=False

class CriancaOut(BaseModel):
    id:str
    nome:str
    idade:int
    responsavel:str


    