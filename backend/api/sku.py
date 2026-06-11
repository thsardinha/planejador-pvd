from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.banco.conexao import obter_sessao
from backend.esquemas.sku import SkuCriar, SkuAtualizar, SkuResposta
from backend.servicos.servico_sku import salvar_sku, obter_todos_skus, obter_sku, alterar_sku

router = APIRouter(prefix="/sku", tags=["SKU"])


@router.post("", response_model=SkuResposta)
def criar(dados: SkuCriar, db: Session = Depends(obter_sessao)):
    try:
        return salvar_sku(db, dados)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("", response_model=list[SkuResposta])
def listar(db: Session = Depends(obter_sessao)):
    return obter_todos_skus(db)


@router.get("/{sku_id}", response_model=SkuResposta)
def buscar(sku_id: int, db: Session = Depends(obter_sessao)):
    try:
        return obter_sku(db, sku_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{sku_id}", response_model=SkuResposta)
def atualizar(sku_id: int, dados: SkuAtualizar, db: Session = Depends(obter_sessao)):
    try:
        return alterar_sku(db, sku_id, dados)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))