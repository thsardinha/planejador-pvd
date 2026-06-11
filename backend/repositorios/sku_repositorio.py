from sqlalchemy.orm import Session
from backend.modelos.sku import SKU


def criar_sku(db: Session, dados):
    sku = SKU(
        codigo=dados.codigo,
        descricao=dados.descricao,
        revestimento=dados.revestimento,
        origem_material=dados.origem_material,
        ativo=dados.ativo,
    )
    db.add(sku)
    db.commit()
    db.refresh(sku)
    return sku


def listar_skus(db: Session):
    return db.query(SKU).order_by(SKU.id).all()


def buscar_sku_por_id(db: Session, sku_id: int):
    return db.query(SKU).filter(SKU.id == sku_id).first()


def atualizar_sku(db: Session, sku: SKU, dados):
    if dados.codigo is not None:
        sku.codigo = dados.codigo
    if dados.descricao is not None:
        sku.descricao = dados.descricao
    if dados.revestimento is not None:
        sku.revestimento = dados.revestimento
    if dados.origem_material is not None:
        sku.origem_material = dados.origem_material
    if dados.ativo is not None:
        sku.ativo = dados.ativo

    db.commit()
    db.refresh(sku)
    return sku