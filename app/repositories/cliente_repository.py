import json
import random
from datetime import datetime, timedelta, timezone

from typing import List, Optional
from sqlalchemy.orm import Session
from faker import Faker
from app.models.entities import Cliente, Transacao
from app.database.connection import Base, engine

fake = Faker('pt_BR')

def init_db():
    Base.metadata.create_all(bind=engine)

class ClienteRepository:
    def __init__(self, db: Session):
        self.db = db

    def carregar_e_popular_json(self, json_path: str) -> int:
        """Carrega clientes.json para o banco relacional."""
        init_db()
        with open(json_path, "r", encoding="utf-8") as f:
            clientes_data = json.load(f)

        inseridos = 0
        for c in clientes_data:
            existing = self.db.query(Cliente).filter(Cliente.id_original == c["id"]).first()
            if existing:
                continue

            dt_cadastro = datetime.strptime(c["data_cadastro"], "%Y-%m-%d")
            novo_cliente = Cliente(
                id_original=c["id"],
                nome=c["nome"],
                idade=c["idade"],
                email=c["email"],
                telefone=c.get("telefone"),
                estado=c["estado"],
                cidade=c.get("cidade"),
                genero=c["genero"],
                data_cadastro=dt_cadastro,
                receita_total=float(c["receita_total"]),
                ativo=c["ativo"]
            )
            self.db.add(novo_cliente)
            inseridos += 1

        self.db.commit()
        return inseridos

    def simular_novas_transacoes(self, quantidade: int = 10) -> List[Transacao]:
        """Engine de simulação: Gera transações dinâmicas para clientes existentes."""
        clientes = self.db.query(Cliente).filter(Cliente.ativo == True).all()
        if not clientes:
            return []

        novas_transacoes = []
        for _ in range(quantidade):
            cliente = random.choice(clientes)
            valor = round(random.uniform(20.0, 1500.0), 2)
            transacao = Transacao(
                cliente_id=cliente.id,
                valor=valor,
                data_transacao=datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(minutes=random.randint(1, 1440)),
                descricao=fake.sentence(nb_words=3)
            )

            cliente.receita_total += valor
            self.db.add(transacao)
            novas_transacoes.append(transacao)

        self.db.commit()
        return novas_transacoes

    def listar_todos(self) -> List[Cliente]:
        return self.db.query(Cliente).all()
