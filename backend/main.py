from fastapi import FastAPI
from backend.api.planejamento import router as planejamento_router
from backend.api.sku import router as sku_router
from backend.modelos import SKU, Maquina, PlanoMensal, PlanoMensalItem, Carga, CargaItem, ProgramacaoDiaria, ProgramacaoDiariaItem  # noqa: F401

app = FastAPI(
    title="Sistema de Planejamento PVD",
    description="API do Sistema de Planejamento PVD",
    version="0.1.0"
)

app.include_router(sku_router)
app.include_router(planejamento_router)


@app.get("/")
def home():
    return {
        "sistema": "Planejamento PVD",
        "status": "online"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }