from sqlalchemy.orm import Session
from backend.repositorios.plano_mensal_repositorio import (
    criar_plano_mensal,
    criar_item_plano_mensal,
    obter_plano_com_itens,
)
from backend.modelos.plano_mensal import PlanoMensal
from backend.modelos.plano_mensal_item import PlanoMensalItem


def salvar_plano_mensal(db: Session, dados):
    if dados.mes < 1 or dados.mes > 12:
        raise ValueError("Mês inválido.")

    if dados.ano < 2000:
        raise ValueError("Ano inválido.")

    plano = criar_plano_mensal(
        db=db,
        mes=dados.mes,
        ano=dados.ano,
        versao=dados.versao,
        criado_por=dados.criado_por,
    )

    for item in dados.itens:
        if item.quantidade <= 0:
            raise ValueError("Quantidade do item deve ser maior que zero.")
        criar_item_plano_mensal(
            db=db,
            plano_id=plano.id,
            sku_id=item.sku_id,
            quantidade=item.quantidade,
        )

    db.commit()

    return obter_plano_com_itens(db, plano.id)