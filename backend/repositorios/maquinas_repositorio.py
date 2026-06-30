from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from backend.modelos.maquina import Maquina


def criar_maquina(db: Session, dados):
    maquina = Maquina(
        nome=dados.nome,
        meta_cargas_dia=dados.meta_cargas_dia,
        tempo_disponivel_dia=dados.tempo_disponivel_dia,
        tempo_carga=dados.tempo_carga,
        capacidade_pecas=dados.capacidade_pecas,
        ativo=dados.ativo,
    )
    db.add(maquina)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise ValueError("Já existe uma máquina com esse nome.")
    db.refresh(maquina)
    return maquina


def listar_maquinas(db: Session):
    return db.query(Maquina).order_by(Maquina.id).all()


def listar_maquinas_ativas(db: Session):
    return db.query(Maquina).filter(Maquina.ativo == True).order_by(Maquina.id).all()


def buscar_maquina_por_id(db: Session, maquina_id: int):
    return db.query(Maquina).filter(Maquina.id == maquina_id).first()


def atualizar_maquina(db: Session, maquina: Maquina, dados):
    if dados.nome is not None:
        maquina.nome = dados.nome
    if dados.meta_cargas_dia is not None:
        maquina.meta_cargas_dia = dados.meta_cargas_dia
    if dados.tempo_disponivel_dia is not None:
        maquina.tempo_disponivel_dia = dados.tempo_disponivel_dia
    if dados.tempo_carga is not None:
        maquina.tempo_carga = dados.tempo_carga
    if dados.capacidade_pecas is not None:
        maquina.capacidade_pecas = dados.capacidade_pecas
    if dados.ativo is not None:
        maquina.ativo = dados.ativo

    db.commit()
    db.refresh(maquina)
    return maquina