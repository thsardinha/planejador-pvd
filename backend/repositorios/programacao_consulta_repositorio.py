from backend.modelos.programacao_diaria import ProgramacaoDiaria
from backend.modelos.programacao_diaria_item import ProgramacaoDiariaItem


def existe_programacao_para_plano(
    db,
    plano_id
):

    return (
        db.query(ProgramacaoDiaria)
        .filter(
            ProgramacaoDiaria.plano_mensal_id == plano_id
        )
        .first()
    )