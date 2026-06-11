from collections import defaultdict


class AgrupadorFamilias:

    @staticmethod
    def gerar_chave_familia(
        revestimento: str,
        origem_material: str
    ) -> str:

        revestimento = (revestimento or "").strip().upper()
        origem_material = (origem_material or "").strip().upper()

        return f"{revestimento}_{origem_material}"

    @staticmethod
    def agrupar(skus: list) -> dict:

        familias = defaultdict(list)

        for sku in skus:

            familia = AgrupadorFamilias.gerar_chave_familia(
                sku["revestimento"],
                sku["origem_material"]
            )

            familias[familia].append(sku)

        return dict(familias)