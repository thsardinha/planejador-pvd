from backend.motor.entidades.carga import Carga
from backend.motor.entidades.item_carga import ItemCarga


def executar():

    carga = Carga(
        familia="PVDF_MDF"
    )

    carga.itens.append(
        ItemCarga(
            sku_id=1,
            codigo="SKU001",
            quantidade=20,
            minutagem_unitaria=6.38
        )
    )

    carga.itens.append(
        ItemCarga(
            sku_id=2,
            codigo="SKU002",
            quantidade=30,
            minutagem_unitaria=5.20
        )
    )

    print()

    print("Família:", carga.familia)

    print("Quantidade:", carga.quantidade_total)

    print("Minutagem:", carga.minutagem_total)

    print()


if __name__ == "__main__":
    executar()