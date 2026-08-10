import pytest
from fastapi.testclient import TestClient
from app.main import app

def test_read_dashboard():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert "CRM Analytics" in response.text

def test_api_kpis():
    with TestClient(app) as client:
        response = client.get("/api/kpis")
        assert response.status_code == 200
        data = response.json()
        assert "total_clientes" in data
        assert "taxa_churn_percentual" in data

def test_api_segmentacao_rfm():
    with TestClient(app) as client:
        response = client.get("/api/segmentacao-rfm")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

def test_api_distribuicao_estados():
    with TestClient(app) as client:
        response = client.get("/api/distribuicao-estados")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

def test_api_simular_compras():
    with TestClient(app) as client:
        response = client.post("/api/simular?quantidade=5")
        assert response.status_code == 200
        data = response.json()
        assert data["novas_transacoes_geradas"] == 5
