from backend.dominio.regras.gerador_cargas import GeradorCargas


def executar():

    saldos = [

        {
            "sku_id": 1,
            "codigo": "SKU001",
            "saldo": 120,
            "minutagem": 6.38
        },

        {
            "sku_id": 2,
            "codigo": "SKU002",
            "saldo": 80,
            "minutagem": 5.20
        }

    ]

    cargas = GeradorCargas.gerar(
        familia="PVDF_MDF",
        saldos=saldos
    )

    print()

    print("Total de cargas:", len(cargas))

    print()

    for indice, carga in enumerate(cargas, start=1):

        print(
            f"Carga {indice}"
        )

        print(
            f"Quantidade: {carga.quantidade_total}"
        )

        print(
            f"Minutagem: {carga.minutagem_total}"
        )

        print()

        for item in carga.itens:

            print(
                item.codigo,
                item.quantidade
            )

        print()
        print("-" * 30)
        print()


if __name__ == "__main__":
    executar()