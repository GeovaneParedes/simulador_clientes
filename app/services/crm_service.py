from typing import Dict, Any, List
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.entities import Cliente, Transacao

class CRMService:
    def __init__(self, db: Session):
        self.db = db

    def obter_kpis_crm(self) -> Dict[str, Any]:
        """Calcula os indicadores chave do CRM."""
        clientes = self.db.query(Cliente).all()
        if not clientes:
            return {
                "total_clientes": 0,
                "clientes_ativos": 0,
                "taxa_churn_percentual": 0.0,
                "receita_total": 0.0,
                "ticket_medio_cliente": 0.0,
                "clientes_vip": 0
            }

        total_clientes = len(clientes)
        ativos = sum(1 for c in clientes if c.ativo)
        inativos = total_clientes - ativos
        taxa_churn = (inativos / total_clientes) * 100.0 if total_clientes > 0 else 0.0
        receita_total = sum(c.receita_total for c in clientes)
        ticket_medio = receita_total / total_clientes if total_clientes > 0 else 0.0
        vip = sum(1 for c in clientes if c.receita_total >= 15000.0)

        return {
            "total_clientes": total_clientes,
            "clientes_ativos": ativos,
            "taxa_churn_percentual": round(taxa_churn, 2),
            "receita_total": round(receita_total, 2),
            "ticket_medio_cliente": round(ticket_medio, 2),
            "clientes_vip": vip
        }

    def obter_distribuicao_por_estado() -> List[Dict[str, Any]]:
        pass

    def segmentacao_rfm(self) -> List[Dict[str, Any]]:
        """Classifica os clientes em segmentos de valor (Champions, Leais, Em Risco, Inativos)."""
        clientes = self.db.query(Cliente).all()
        segmentos = []
        for c in clientes:
            if c.receita_total >= 15000.0 and c.ativo:
                categoria = "Champions (VIP)"
            elif c.receita_total >= 5000.0 and c.ativo:
                categoria = "Clientes Leais"
            elif c.ativo:
                categoria = "Promissores"
            else:
                categoria = "Em Risco / Inativos"

            segmentos.append({
                "cliente_id": c.id,
                "nome": c.nome,
                "estado": c.estado,
                "receita_total": round(c.receita_total, 2),
                "categoria": categoria
            })
        return segmentos

    def obter_distribuicao_por_estado(self) -> List[Dict[str, Any]]:
        """Retorna a contagem de clientes e receita total acumulada por Estado (UF)."""
        resultados = (
            self.db.query(
                Cliente.estado,
                func.count(Cliente.id).label("total_clientes"),
                func.sum(Cliente.receita_total).label("receita_estado")
            )
            .group_by(Cliente.estado)
            .order_by(func.sum(Cliente.receita_total).desc())
            .all()
        )
        return [
            {
                "estado": r.estado,
                "total_clientes": int(r.total_clientes),
                "receita_estado": round(float(r.receita_estado), 2)
            }
            for r in resultados
        ]
