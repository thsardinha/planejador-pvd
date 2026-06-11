from backend.motor.agrupador_familias import AgrupadorFamilias


def executar():

    skus = [

        {
            "codigo": "SKU001",
            "revestimento": "PVDF",
            "origem_material": "MDF"
        },

        {
            "codigo": "SKU002",
            "revestimento": "PVDF",
            "origem_material": "MDF"
        },

        {
            "codigo": "SKU003",
            "revestimento": "BP",
            "origem_material": "MDP"
        }

    ]

    resultado = AgrupadorFamilias.agrupar(skus)

    print(resultado)


if __name__ == "__main__":
    executar()