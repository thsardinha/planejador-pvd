from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.banco.conexao import obter_sessao
from backend.modelos.programacao_diaria import ProgramacaoDiaria
from backend.modelos.programacao_diaria_item import ProgramacaoDiariaItem
from backend.modelos.carga import Carga
from backend.modelos.maquina import Maquina

router = APIRouter(prefix="/programacao", tags=["Programação"])


@router.get("/{plano_id}")
def listar_programacao_do_plano(plano_id: int, db: Session = Depends(obter_sessao)):
    programacoes = (
        db.query(ProgramacaoDiaria)
        .filter(ProgramacaoDiaria.plano_mensal_id == plano_id)
        .order_by(ProgramacaoDiaria.data_programacao)
        .all()
    )

    if not programacoes:
        raise HTTPException(status_code=404, detail="Nenhuma programação encontrada para este plano.")

    retorno = []

    for programacao in programacoes:
        itens = (
            db.query(ProgramacaoDiariaItem, Carga, Maquina)
            .join(Carga, Carga.id == ProgramacaoDiariaItem.carga_id)
            .join(Maquina, Maquina.id == ProgramacaoDiariaItem.maquina_id)
            .filter(ProgramacaoDiariaItem.programacao_diaria_id == programacao.id)
            .order_by(ProgramacaoDiariaItem.sequencia_carga)
            .all()
        )

        retorno_itens = []
        for item, carga, maquina in itens:
            retorno_itens.append(
                {
                    "carga_id": item.carga_id,
                    "maquina": maquina.nome,
                    "sequencia_carga": item.sequencia_carga,
                    "minutagem": item.minutagem,
                    "familia": carga.familia,
                }
            )

        retorno.append(
            {
                "data_programacao": programacao.data_programacao,
                "status": programacao.status,
                "itens": retorno_itens,
            }
        )

    return {
        "plano_id": plano_id,
        "programacoes": retorno,
    }