from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from backend.banco.base import Base


class SKU(Base):
    __tablename__ = "sku"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(100), unique=True, index=True, nullable=False)
    descricao = Column(String(255), nullable=True)
    revestimento = Column(String(100), nullable=True)
    origem_material = Column(String(100), nullable=True)
    ativo = Column(Boolean, default=True, nullable=False)
    criado_em = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    atualizado_em = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)