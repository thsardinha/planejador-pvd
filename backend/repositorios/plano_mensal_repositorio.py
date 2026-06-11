from sqlalchemy.orm import Session
from backend.modelos.plano_mensal import PlanoMensal
from backend.modelos.plano_mensal_item import PlanoMensalItem
from backend.modelos.sku import SKU


def criar_plano_mensal(db: Session, mes: int, ano: int, versao: int, criado_por: str | None):
    plano = PlanoMensal(
        mes=mes,
        ano=ano,
        versao=versao,
        criado_por=criado_por,
        status="RASCUNHO",
    )
    db.add(plano)
    db.flush()
    return plano


def criar_item_plano_mensal(db: Session, plano_id: int, sku_id: int, quantidade: int):
    item = PlanoMensalItem(
        plano_mensal_id=plano_id,
        sku_id=sku_id,
        quantidade=quantidade,
    )
    db.add(item)
    return item


def obter_plano_com_itens(db: Session, plano_id: int):
    plano = db.query(PlanoMensal).filter(PlanoMensal.id == plano_id).first()
    if not plano:
        return None

    itens = (
        db.query(PlanoMensalItem)
        .filter(PlanoMensalItem.plano_mensal_id == plano_id)
        .all()
    )
    return plano, itens

def obter_itens_plano_com_sku(db, plano_id: int):

    resultado = (
        db.query(
            PlanoMensalItem,
            SKU
        )
        .join(
            SKU,
            SKU.id == PlanoMensalItem.sku_id
        )
        .filter(
            PlanoMensalItem.plano_mensal_id == plano_id
        )
        .all()
    )

    return resultado