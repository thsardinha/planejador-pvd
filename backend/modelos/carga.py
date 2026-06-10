from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from backend.banco.base import Base


class Carga(Base):
    __tablename__ = "carga"

    id = Column(Integer, primary_key=True, index=True)
    plano_mensal_id = Column(Integer, ForeignKey("plano_mensal.id"), nullable=False)
    familia = Column(String(150), nullable=False)
    quantidade_total = Column(Integer, nullable=False)
    minutagem_total = Column(Float, nullable=False)
    status = Column(String(30), nullable=False, default="GERADA")
    criado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    atualizado_em = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)