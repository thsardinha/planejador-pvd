from sqlalchemy import Column, Integer, Float, ForeignKey
from backend.banco.base import Base


class CargaItem(Base):
    __tablename__ = "carga_item"

    id = Column(Integer, primary_key=True, index=True)
    carga_id = Column(Integer, ForeignKey("carga.id"), nullable=False)
    sku_id = Column(Integer, ForeignKey("sku.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    minutagem = Column(Float, nullable=False)