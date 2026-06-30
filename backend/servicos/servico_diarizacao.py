from datetime import date

from backend.dominio.regras.diarizador import Diarizador

from backend.repositorios.cargas_repositorio import (
    listar_cargas_por_plano
)

from backend.repositorios.maquinas_repositorio import (
    listar_maquinas_ativas
)

from backend.repositorios.programacao_diaria_repositorio import (
    criar_programacao_diaria,
    criar_programacao_diaria_item
)

from backend.repositorios.programacao_consulta_repositorio import (
    existe_programacao_para_plano
)


def gerar_programacao(
    db,
    plano_id: int
):

    programacao_existente = existe_programacao_para_plano(
        db,
        plano_id
    )

    if programacao_existente:
        raise ValueError(
            "Já existe programação para este plano."
        )

    cargas = listar_cargas_por_plano(
        db,
        plano_id
    )

    if not cargas:
        raise ValueError(
            "Plano não possui cargas geradas."
        )

    maquinas = listar_maquinas_ativas(
        db
    )

    if not maquinas:
        raise ValueError("Não existem máquinas ativas cadastradas.")
    
    if not maquinas:
        raise ValueError("Lista de máquinas vazia.")

    programacoes = Diarizador.gerar(
        cargas=cargas,
        maquinas=maquinas,
        data_inicial=date.today()
    )

    programacoes_por_data = {}

    for p in programacoes:

        if p.data_programacao not in programacoes_por_data:

            programacoes_por_data[
                p.data_programacao
            ] = criar_programacao_diaria(
                db,
                p.data_programacao,
                plano_id
            )

    for p in programacoes:

        programacao_db = programacoes_por_data[
            p.data_programacao
        ]

        carga = next(
            c
            for c in cargas
            if c.id == p.carga_id
        )

        criar_programacao_diaria_item(
            db=db,
            programacao_diaria_id=programacao_db.id,
            carga_id=p.carga_id,
            maquina_id=p.maquina_id,
            sequencia_carga=p.sequencia_carga,
            minutagem=carga.minutagem_total
        )

    db.commit()

    return {
        "dias_gerados": len(programacoes_por_data),
        "programacoes": len(programacoes)
    }