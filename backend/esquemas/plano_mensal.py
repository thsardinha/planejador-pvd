from pydantic import BaseModel
from typing import List, Optional


class ItemPlanoMensalBase(BaseModel):
    sku_id: int
    quantidade: int


class PlanoMensalCriar(BaseModel):
    mes: int
    ano: int
    versao: int = 1
    criado_por: Optional[str] = None
    itens: List[ItemPlanoMensalBase]


class ItemPlanoMensalResposta(BaseModel):
    sku_id: int
    quantidade: int


class PlanoMensalResposta(BaseModel):
    id: int
    mes: int
    ano: int
    versao: int
    status: str
    criado_por: Optional[str] = None
    itens: List[ItemPlanoMensalResposta]

    class Config:
        from_attributes = True