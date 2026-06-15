from backend.repositorios.carga_repositorio import criar_carga, criar_item_carga


def salvar_cargas_geradas(db, plano_mensal_id: int, cargas):
    total_cargas = 0
    total_itens = 0

    for carga in cargas:
        carga_db = criar_carga(
            db=db,
            plano_mensal_id=plano_mensal_id,
            familia=carga.familia,
            quantidade_total=carga.quantidade_total,
            minutagem_total=carga.minutagem_total,
            status="GERADA",
        )

        for item in carga.itens:
            criar_item_carga(
                db=db,
                carga_id=carga_db.id,
                sku_id=item.sku_id,
                quantidade=item.quantidade,
                minutagem=item.minutagem_total,
            )
            total_itens += 1

        total_cargas += 1

    db.commit()

    return {
        "plano_mensal_id": plano_mensal_id,
        "cargas_geradas": total_cargas,
        "itens_gerados": total_itens,
    }