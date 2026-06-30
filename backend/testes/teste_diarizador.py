from datetime import date
from types import SimpleNamespace

from backend.dominio.regras.diarizador import Diarizador


def executar():

    maquinas = [

        SimpleNamespace(
            id=1,
            nome="HC566",
            meta_cargas_dia=4
        ),

        SimpleNamespace(
            id=2,
            nome="HC567",
            meta_cargas_dia=4
        ),

        SimpleNamespace(
            id=3,
            nome="HC582",
            meta_cargas_dia=4
        ),

        SimpleNamespace(
            id=4,
            nome="HC583",
            meta_cargas_dia=4
        ),

        SimpleNamespace(
            id=5,
            nome="HC584",
            meta_cargas_dia=5
        )
    ]

    cargas = []

    for i in range(42):

        cargas.append(
            SimpleNamespace(
                id=i + 1
            )
        )

    programacoes = Diarizador.gerar(
        cargas=cargas,
        maquinas=maquinas,
        data_inicial=date(2026, 6, 1)
    )

    print()

    print("Total Programações:", len(programacoes))

    print()

    for p in programacoes[:25]:

        print(
            p.data_programacao,
            p.maquina_id,
            p.carga_id,
            p.sequencia_carga
        )

    print()


if __name__ == "__main__":
    executar()