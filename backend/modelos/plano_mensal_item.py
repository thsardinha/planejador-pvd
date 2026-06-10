from sqlalchemy import Column, Integer, ForeignKey
from backend.banco.base import Base


class PlanoMensalItem(Base):
    __tablename__ = "plano_mensal_item"

    id = Column(Integer, primary_key=True, index=True)
    plano_mensal_id = Column(Integer, ForeignKey("plano_mensal.id"), nullable=False)
    sku_id = Column(Integer, ForeignKey("sku.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)