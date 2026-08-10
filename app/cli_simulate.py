from app.database.connection import SessionLocal
from app.repositories.cliente_repository import ClienteRepository, init_db

def main():
    print("🚀 Carregando base de clientes.json no banco SQLite...")
    init_db()
    session = SessionLocal()
    try:
        repo = ClienteRepository(session)
        inseridos = repo.carregar_e_popular_json("clientes.json")
        print(f"✅ Carga concluída! Clientes na base: {inseridos}")

        print("⚡ Iniciando simulação de tráfego (gerando 15 novas transações aleatórias)...")
        txs = repo.simular_novas_transacoes(quantidade=15)
        print(f"🎉 Simulação concluída com sucesso! Total de {len(txs)} novas compras registradas.")
        for tx in txs[:5]:
            print(f" 💳 Cliente ID #{tx.cliente_id} comprou R$ {tx.valor:.2f} ({tx.descricao})")
    finally:
        session.close()

if __name__ == "__main__":
    main()
