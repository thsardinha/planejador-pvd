from backend.modelos.maquina import Maquina


def listar_maquinas_ativas(db):

    return (
        db.query(Maquina)
        .filter(
            Maquina.ativo == True
        )
        .order_by(Maquina.id)
        .all()
    )