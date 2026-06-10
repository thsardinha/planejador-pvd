from sqlalchemy import Column, Integer, Float, ForeignKey
from backend.banco.base import Base


class ProgramacaoDiariaItem(Base):
    __tablename__ = "programacao_diaria_item"

    id = Column(Integer, primary_key=True, index=True)
    programacao_diaria_id = Column(Integer, ForeignKey("programacao_diaria.id"), nullable=False)
    carga_id = Column(Integer, ForeignKey("carga.id"), nullable=False)
    maquina_id = Column(Integer, ForeignKey("maquina.id"), nullable=False)
    sequencia_carga = Column(Integer, nullable=False)
    minutagem = Column(Float, nullable=False)