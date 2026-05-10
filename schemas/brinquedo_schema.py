from pydantic import BaseModel

class BrinquedoCreate(BaseModel):
    nome:str
    categoria:str
    faixa_etaria_minima:int
    disponivel:bool=True

class BrinquedoOut(BaseModel):
    id:str
    nome:str
    categoria:str
    faixa_etaria_minima:int
    disponivel:bool = True


    class Config:
        from_attributes=True