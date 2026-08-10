from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    id_original = Column(Integer, unique=True, index=True, nullable=True)
    nome = Column(String(150), nullable=False)
    idade = Column(Integer, nullable=False)
    email = Column(String(150), nullable=False)
    telefone = Column(String(50), nullable=True)
    estado = Column(String(10), nullable=False, index=True)
    cidade = Column(String(100), nullable=True)
    genero = Column(String(10), nullable=False)
    data_cadastro = Column(DateTime, nullable=False, default=datetime.utcnow)
    receita_total = Column(Float, nullable=False, default=0.0)
    ativo = Column(Boolean, nullable=False, default=True)

    transacoes = relationship("Transacao", back_populates="cliente", cascade="all, delete-orphan")

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"), nullable=False)
    valor = Column(Float, nullable=False)
    data_transacao = Column(DateTime, nullable=False, default=datetime.utcnow, index=True)
    descricao = Column(String(200), nullable=True)

    cliente = relationship("Cliente", back_populates="transacoes")
