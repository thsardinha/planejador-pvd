from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.banco.conexao import obter_sessao
from backend.esquemas.maquinas import MaquinaCriar, MaquinaAtualizar, MaquinaResposta
from backend.servicos.servico_maquinas import (
    salvar_maquina,
    obter_todas_maquinas,
    obter_maquina,
    alterar_maquina,
    obter_maquinas_ativas,
)

router = APIRouter(prefix="/maquinas", tags=["Máquinas"])


@router.post("", response_model=MaquinaResposta)
def criar(dados: MaquinaCriar, db: Session = Depends(obter_sessao)):
    try:
        return salvar_maquina(db, dados)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("", response_model=list[MaquinaResposta])
def listar(db: Session = Depends(obter_sessao)):
    return obter_todas_maquinas(db)


@router.get("/ativas", response_model=list[MaquinaResposta])
def listar_ativas(db: Session = Depends(obter_sessao)):
    return obter_maquinas_ativas(db)


@router.get("/{maquina_id}", response_model=MaquinaResposta)
def buscar(maquina_id: int, db: Session = Depends(obter_sessao)):
    try:
        return obter_maquina(db, maquina_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/{maquina_id}", response_model=MaquinaResposta)
def atualizar(maquina_id: int, dados: MaquinaAtualizar, db: Session = Depends(obter_sessao)):
    try:
        return alterar_maquina(db, maquina_id, dados)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))