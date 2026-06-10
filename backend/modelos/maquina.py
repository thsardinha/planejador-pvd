from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from backend.banco.base import Base


class Maquina(Base):
    __tablename__ = "maquina"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), unique=True, nullable=False, index=True)
    meta_cargas_dia = Column(Integer, nullable=False)
    tempo_disponivel_dia = Column(Integer, nullable=False)
    tempo_carga = Column(Integer, nullable=False)
    capacidade_pecas = Column(Integer, nullable=False, default=50)
    ativo = Column(Boolean, default=True, nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    atualizado_em = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)