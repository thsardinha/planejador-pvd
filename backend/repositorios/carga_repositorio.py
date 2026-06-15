from sqlalchemy.orm import Session
from backend.modelos.carga import Carga
from backend.modelos.carga_item import CargaItem


def criar_carga(db: Session, plano_mensal_id: int, familia: str, quantidade_total: int, minutagem_total: float, status: str = "GERADA"):
    carga = Carga(
        plano_mensal_id=plano_mensal_id,
        familia=familia,
        quantidade_total=quantidade_total,
        minutagem_total=minutagem_total,
        status=status,
    )
    db.add(carga)
    db.flush()
    return carga


def criar_item_carga(db: Session, carga_id: int, sku_id: int, quantidade: int, minutagem: float):
    item = CargaItem(
        carga_id=carga_id,
        sku_id=sku_id,
        quantidade=quantidade,
        minutagem=minutagem,
    )
    db.add(item)
    return item