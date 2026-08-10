from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.database.connection import get_db, SessionLocal
from app.repositories.cliente_repository import ClienteRepository, init_db
from app.services.crm_service import CRMService

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    db = SessionLocal()
    try:
        repo = ClienteRepository(db)
        repo.carregar_e_popular_json("clientes.json")
    finally:
        db.close()
    yield

app = FastAPI(
    title="Simulador de Clientes - CRM Analytics API",
    description="API REST, Engine de Simulação de Tráfego e Dashboard CRM",
    version="1.0.0",
    lifespan=lifespan
)

@app.middleware("http")
def db_session_middleware(request, call_next):
    init_db()
    response = call_next(request)
    return response

@app.get("/", response_class=HTMLResponse)
def read_dashboard():
    with open("app/templates/dashboard.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/kpis")
def get_kpis(db: Session = Depends(get_db)):
    service = CRMService(db)
    return service.obter_kpis_crm()

@app.get("/api/segmentacao-rfm")
def get_segmentacao_rfm(db: Session = Depends(get_db)):
    service = CRMService(db)
    return service.segmentacao_rfm()

@app.get("/api/distribuicao-estados")
def get_distribuicao_estados(db: Session = Depends(get_db)):
    service = CRMService(db)
    return service.obter_distribuicao_por_estado()

@app.post("/api/simular")
def trigger_simulation(quantidade: int = 10, db: Session = Depends(get_db)):
    repo = ClienteRepository(db)
    novas_txs = repo.simular_novas_transacoes(quantidade=quantidade)
    return {
        "status": "success",
        "novas_transacoes_geradas": len(novas_txs)
    }
