from pydantic import BaseModel, computed_field
from datetime import date, timedelta
class EmprestimoCreate(BaseModel):
    crianca_id:str
    brinquedo_id:str
    data_retirado:date

class EmprestimoOut(BaseModel):
    id:str
    crianca_id:str
    brinquedo_id:str
    data_retirado:date
    status:str
    multa:float

    model_config = {"from_attributes":True}

    @computed_field
    @property
    def data_para_entrega(self)->date:
        return self.data_retirado + timedelta(days=7)