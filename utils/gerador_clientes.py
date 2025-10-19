#!/usr/bin/env python3
from faker import Faker
import random
import json
from pathlib import Path

faker = Faker("pt_BR")
random.seed(42)
Faker.seed(42)

def gerar_clientes(qtd: int = 200) -> list[dict]:
    clientes = []
    for i in range(1, qtd + 1):
        cliente = {
            "id": i,
            "nome": faker.name(),
            "idade": random.randint(18, 70),
            "email": faker.email(),
            "telefone": faker.phone_number(),
            "estado": faker.estado_sigla(),
            "cidade": faker.city(),
            "genero": random.choice(["M", "F"]),
            "data_cadastro": str(faker.date_between(start_date="-3y", end_date="today")),
            "receita_total": round(random.uniform(500, 20000), 2),
            "ativo": random.choice([True, True, True, False])  # 75% ativos
        }
        clientes.append(cliente)
    return clientes


def salvar_json(clientes: list[dict], arquivo: Path):
    arquivo.parent.mkdir(parents=True, exist_ok=True)
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    destino = Path(__file__).resolve().parents[1] / "clientes.json"
    clientes = gerar_clientes()
    salvar_json(clientes, destino)
    print(f"Arquivo gerado em: {destino}")
