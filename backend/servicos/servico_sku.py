from backend.repositorios.sku_repositorio import (
    criar_sku,
    listar_skus,
    buscar_sku_por_id,
    atualizar_sku,
)


def salvar_sku(db, dados):
    if not dados.codigo or not dados.codigo.strip():
        raise ValueError("Código do SKU é obrigatório.")

    return criar_sku(db, dados)


def obter_todos_skus(db):
    return listar_skus(db)


def obter_sku(db, sku_id: int):
    sku = buscar_sku_por_id(db, sku_id)
    if not sku:
        raise ValueError("SKU não encontrado.")
    return sku


def alterar_sku(db, sku_id: int, dados):
    sku = buscar_sku_por_id(db, sku_id)
    if not sku:
        raise ValueError("SKU não encontrado.")
    return atualizar_sku(db, sku, dados)