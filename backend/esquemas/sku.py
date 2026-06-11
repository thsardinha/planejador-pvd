from pydantic import BaseModel
from typing import Optional


class SkuBase(BaseModel):
    codigo: str
    descricao: Optional[str] = None
    revestimento: Optional[str] = None
    origem_material: Optional[str] = None
    ativo: bool = True


class SkuCriar(SkuBase):
    pass


class SkuAtualizar(BaseModel):
    codigo: Optional[str] = None
    descricao: Optional[str] = None
    revestimento: Optional[str] = None
    origem_material: Optional[str] = None
    ativo: Optional[bool] = None


class SkuResposta(SkuBase):
    id: int

    class Config:
        from_attributes = True