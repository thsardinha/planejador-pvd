from datetime import date, timedelta

from backend.dominio.entidades.programacao import Programacao


class Diarizador:

    @classmethod
    def gerar(
        cls,
        cargas,
        maquinas,
        data_inicial: date
    ):

        programacoes = []

        data_atual = data_inicial

        indice_carga = 0

        while indice_carga < len(cargas):

            for rodada in range(
                max(
                    maquina.meta_cargas_dia
                    for maquina in maquinas
                )
            ):

                for maquina in maquinas:

                    if rodada >= maquina.meta_cargas_dia:
                        continue

                    if indice_carga >= len(cargas):
                        break

                    carga = cargas[indice_carga]

                    programacoes.append(

                        Programacao(
                            data_programacao=data_atual,
                            maquina_id=maquina.id,
                            carga_id=carga.id,
                            sequencia_carga=rodada + 1
                        )

                    )

                    indice_carga += 1

            data_atual += timedelta(days=1)

        return programacoes