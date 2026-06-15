from backend.modelos.carga import Carga


def listar_cargas_por_plano(
    db,
    plano_mensal_id
):
    return (
        db.query(Carga)
        .filter(
            Carga.plano_mensal_id == plano_mensal_id
        )
        .order_by(Carga.id)
        .all()
    )