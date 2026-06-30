from backend.repositorios.maquinas_repositorio import (
    criar_maquina,
    listar_maquinas,
    listar_maquinas_ativas,
    buscar_maquina_por_id,
    atualizar_maquina,
)


def salvar_maquina(db, dados):
    if not dados.nome or not dados.nome.strip():
        raise ValueError("Nome da máquina é obrigatório.")
    return criar_maquina(db, dados)


def obter_todas_maquinas(db):
    return listar_maquinas(db)


def obter_maquinas_ativas(db):
    return listar_maquinas_ativas(db)


def obter_maquina(db, maquina_id: int):
    maquina = buscar_maquina_por_id(db, maquina_id)
    if not maquina:
        raise ValueError("Máquina não encontrada.")
    return maquina


def alterar_maquina(db, maquina_id: int, dados):
    maquina = buscar_maquina_por_id(db, maquina_id)
    if not maquina:
        raise ValueError("Máquina não encontrada.")
    return atualizar_maquina(db, maquina, dados)