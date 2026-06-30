from pydantic import BaseModel
from typing import Optional


class MaquinaBase(BaseModel):
    nome: str
    meta_cargas_dia: int
    tempo_disponivel_dia: int
    tempo_carga: int
    capacidade_pecas: int = 50
    ativo: bool = True


class MaquinaCriar(MaquinaBase):
    pass


class MaquinaAtualizar(BaseModel):
    nome: Optional[str] = None
    meta_cargas_dia: Optional[int] = None
    tempo_disponivel_dia: Optional[int] = None
    tempo_carga: Optional[int] = None
    capacidade_pecas: Optional[int] = None
    ativo: Optional[bool] = None


class MaquinaResposta(MaquinaBase):
    id: int

    class Config:
        from_attributes = True