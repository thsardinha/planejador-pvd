from sqlalchemy import Column, Integer, String, DateTime, func
from backend.banco.base import Base


class PlanoMensal(Base):
    __tablename__ = "plano_mensal"

    id = Column(Integer, primary_key=True, index=True)
    mes = Column(Integer, nullable=False)
    ano = Column(Integer, nullable=False)
    versao = Column(Integer, nullable=False, default=1)
    status = Column(String(30), nullable=False, default="RASCUNHO")
    criado_por = Column(String(100), nullable=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    atualizado_em = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)