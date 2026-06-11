from backend.motor.agrupador_familias import AgrupadorFamilias
from backend.motor.gerador_cargas import GeradorCargas

from backend.repositorios.plano_mensal_repositorio import (
    obter_itens_plano_com_sku
)


def gerar_cargas_plano(
    db,
    plano_id: int
):

    itens = obter_itens_plano_com_sku(
        db,
        plano_id
    )

    if not itens:
        raise ValueError(
            "Plano não possui itens."
        )

    skus_motor = []

    for item, sku in itens:

        skus_motor.append(
            {
                "sku_id": sku.id,
                "codigo": sku.codigo,
                "revestimento": sku.revestimento,
                "origem_material": sku.origem_material,
                "saldo": item.quantidade,
                "minutagem": 0
            }
        )

    familias = AgrupadorFamilias.agrupar(
        skus_motor
    )

    cargas = []

    for familia, saldos in familias.items():

        cargas_familia = GeradorCargas.gerar(
            familia=familia,
            saldos=saldos
        )

        cargas.extend(
            cargas_familia
        )

    return cargas