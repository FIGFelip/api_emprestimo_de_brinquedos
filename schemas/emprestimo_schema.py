from pydantic import BaseModel

class EmprestimoCreate(BaseModel):
    crianca_id:str
    brinquedo_id:str
    datas:int
    status:str
    multa:float

class EmprestimoOut(BaseModel):
    id:str
    crianca_id:str
    brinquedo_id:str
    datas:int
    status:str
    multa:float

    class Config:
        from_attributes=True