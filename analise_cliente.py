#!/usr/bin/env python3
import json
from pathlib import Path
from statistics import mean
from collections import Counter

ARQUIVO_CLIENTES = Path(__file__).parent / "clientes.json"


def carregar_clientes() -> list[dict]:
    with open(ARQUIVO_CLIENTES, "r", encoding="utf-8") as f:
        return json.load(f)


def analisar_clientes(clientes: list[dict]):
    total = len(clientes)
    ativos = sum(1 for c in clientes if c["ativo"])
    media_idade = mean(c["idade"] for c in clientes)
    media_receita = mean(c["receita_total"] for c in clientes)
    total_receita = sum(c["receita_total"] for c in clientes)

    por_estado = Counter(c["estado"] for c in clientes)
    por_genero = Counter(c["genero"] for c in clientes)

    vip = [c for c in clientes if c["receita_total"] > 15000]

    print(f"Total de clientes: {total}")
    print(f"Ativos: {ativos} ({ativos/total:.1%})")
    print(f"Média de idade: {media_idade:.1f}")
    print(f"Receita total: R$ {total_receita:,.2f}")
    print(f"Média de receita por cliente: R$ {media_receita:,.2f}")
    print(f"Clientes VIP (>R$ 15.000): {len(vip)}")
    print(f"Distribuição por estado: {dict(por_estado)}")
    print(f"Distribuição por gênero: {dict(por_genero)}")


if __name__ == "__main__":
    clientes = carregar_clientes()
    analisar_clientes(clientes)
