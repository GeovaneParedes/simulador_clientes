import os
import pytest
from app.database.connection import Base, engine, SessionLocal
from app.repositories.cliente_repository import ClienteRepository

@pytest.fixture
def db_session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_carregar_clientes_json(db_session):
    repo = ClienteRepository(db_session)
    inseridos = repo.carregar_e_popular_json("clientes.json")
    assert inseridos > 0

    clientes = repo.listar_todos()
    assert len(clientes) == inseridos

def test_simular_transacoes(db_session):
    repo = ClienteRepository(db_session)
    repo.carregar_e_popular_json("clientes.json")

    novas_txs = repo.simular_novas_transacoes(quantidade=5)
    assert len(novas_txs) == 5
    assert novas_txs[0].valor > 0
