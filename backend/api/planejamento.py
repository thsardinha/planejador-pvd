from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.banco.conexao import obter_sessao
from backend.esquemas.plano_mensal import PlanoMensalCriar
from backend.servicos.servico_plano_mensal import salvar_plano_mensal

router = APIRouter(prefix="/planejamento", tags=["Planejamento"])


@router.post("/planos-mensais")
def criar_plano_mensal(dados: PlanoMensalCriar, db: Session = Depends(obter_sessao)):
    try:
        resultado = salvar_plano_mensal(db, dados)
        if not resultado:
            raise HTTPException(status_code=404, detail="Plano não encontrado após gravação.")

        plano, itens = resultado

        return {
            "id": plano.id,
            "mes": plano.mes,
            "ano": plano.ano,
            "versao": plano.versao,
            "status": plano.status,
            "criado_por": plano.criado_por,
            "itens": [
                {
                    "sku_id": item.sku_id,
                    "quantidade": item.quantidade,
                }
                for item in itens
            ],
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))