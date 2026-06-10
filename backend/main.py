from fastapi import FastAPI
from backend.modelos import SKU  # noqa: F401

app = FastAPI(
    title="Sistema de Planejamento PVD",
    description="API do Sistema de Planejamento PVD",
    version="0.1.0"
)


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