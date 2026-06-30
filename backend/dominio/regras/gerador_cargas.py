from backend.dominio.entidades.carga import Carga
from backend.dominio.entidades.item_carga import ItemCarga


class GeradorCargas:

    CAPACIDADE_MAXIMA = 50

    @classmethod
    def gerar(
        cls,
        familia: str,
        saldos: list
    ) -> list[Carga]:

        cargas = []

        saldos_trabalho = [
            saldo.copy()
            for saldo in saldos
        ]

        while any(
            item["saldo"] > 0
            for item in saldos_trabalho
        ):

            carga = Carga(
                familia=familia
            )

            capacidade_restante = cls.CAPACIDADE_MAXIMA

            for item in saldos_trabalho:

                if capacidade_restante <= 0:
                    break

                if item["saldo"] <= 0:
                    continue

                quantidade = min(
                    item["saldo"],
                    capacidade_restante
                )

                carga.itens.append(
                    ItemCarga(
                        sku_id=item["sku_id"],
                        codigo=item["codigo"],
                        quantidade=quantidade,
                        minutagem_unitaria=item["minutagem"]
                    )
                )

                item["saldo"] -= quantidade
                capacidade_restante -= quantidade

            cargas.append(carga)

        return cargas