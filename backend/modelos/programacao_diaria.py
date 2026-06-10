from sqlalchemy import Column, Integer, Date, String, ForeignKey, DateTime, func
from backend.banco.base import Base


class ProgramacaoDiaria(Base):
    __tablename__ = "programacao_diaria"

    id = Column(Integer, primary_key=True, index=True)
    data_programacao = Column(Date, nullable=False)
    plano_mensal_id = Column(Integer, ForeignKey("plano_mensal.id"), nullable=False)
    status = Column(String(30), nullable=False, default="RASCUNHO")
    criado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    atualizado_em = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)