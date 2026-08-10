import pytest
from app.database.connection import Base, engine, SessionLocal
from app.repositories.cliente_repository import ClienteRepository
from app.services.crm_service import CRMService

@pytest.fixture
def db_populated():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    repo = ClienteRepository(session)
    repo.carregar_e_popular_json("clientes.json")
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_kpis_crm(db_populated):
    service = CRMService(db_populated)
    kpis = service.obter_kpis_crm()

    assert kpis["total_clientes"] == 200
    assert kpis["clientes_ativos"] > 0
    assert kpis["receita_total"] > 0
    assert kpis["ticket_medio_cliente"] > 0

def test_segmentacao_rfm(db_populated):
    service = CRMService(db_populated)
    segmentos = service.segmentacao_rfm()

    assert len(segmentos) == 200
    assert "categoria" in segmentos[0]

def test_distribuicao_por_estado(db_populated):
    service = CRMService(db_populated)
    estados = service.obter_distribuicao_por_estado()

    assert len(estados) > 0
    assert "estado" in estados[0]
    assert "receita_estado" in estados[0]
