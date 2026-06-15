from backend.modelos.programacao_diaria import ProgramacaoDiaria
from backend.modelos.programacao_diaria_item import ProgramacaoDiariaItem


def criar_programacao_diaria(
    db,
    data_programacao,
    plano_mensal_id
):
    programacao = ProgramacaoDiaria(
        data_programacao=data_programacao,
        plano_mensal_id=plano_mensal_id,
        status="RASCUNHO"
    )

    db.add(programacao)
    db.flush()

    return programacao


def criar_programacao_diaria_item(
    db,
    programacao_diaria_id,
    carga_id,
    maquina_id,
    sequencia_carga,
    minutagem
):
    item = ProgramacaoDiariaItem(
        programacao_diaria_id=programacao_diaria_id,
        carga_id=carga_id,
        maquina_id=maquina_id,
        sequencia_carga=sequencia_carga,
        minutagem=minutagem
    )

    db.add(item)

    return item