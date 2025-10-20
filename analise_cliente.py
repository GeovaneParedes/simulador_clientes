import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

ARQUIVO_CLIENTES = Path(__file__).parent / "clientes.json"

def carregar_clientes() -> pd.DataFrame:
    """Carrega os clientes em um DataFrame pandas."""
    return pd.read_json(ARQUIVO_CLIENTES)

def resumo_estatistico(df: pd.DataFrame):
    """Gera KPIs e resumo geral."""
    total = len(df)
    ativos = df["ativo"].sum()
    media_idade = df["idade"].mean()
    media_receita = df["receita_total"].mean()
    receita_total = df["receita_total"].sum()
    vip = df[df["receita_total"] > 15000]

    print("\n📊 RESUMO GERAL")
    print(f"Total de clientes: {total}")
    print(f"Ativos: {ativos} ({ativos/total:.1%})")
    print(f"Média de idade: {media_idade:.1f}")
    print(f"Receita total: R$ {receita_total:,.2f}")
    print(f"Média por cliente: R$ {media_receita:,.2f}")
    print(f"Clientes VIP (> R$15.000): {len(vip)}\n")

def grafico_clientes_por_estado(df: pd.DataFrame):
    """Exibe gráfico de barras com clientes por estado."""
    df_estado = df["estado"].value_counts().sort_index()
    df_estado.plot(kind="bar", figsize=(8, 4), title="Clientes por Estado", xlabel="Estado", ylabel="Quantidade")
    plt.tight_layout()
    plt.show()

def grafico_receita_por_estado(df: pd.DataFrame):
    """Exibe gráfico da soma de receita por estado."""
    df_receita = df.groupby("estado")["receita_total"].sum().sort_values(ascending=False)
    df_receita.plot(kind="bar", figsize=(8, 4), title="Receita Total por Estado", xlabel="Estado", ylabel="Receita (R$)")
    plt.tight_layout()
    plt.show()

def grafico_genero(df: pd.DataFrame):
    """Exibe gráfico de pizza da distribuição de gênero."""
    df["genero"].value_counts().plot(
        kind="pie",
        autopct="%.1f%%",
        startangle=90,
        figsize=(5, 5),
        title="Distribuição por Gênero"
    )
    plt.ylabel("")  # remove label padrão
    plt.tight_layout()
    plt.show()

def grafico_receita_faixas(df: pd.DataFrame):
    """Mostra distribuição de clientes por faixa de receita."""
    bins = [0, 5000, 10000, 15000, 20000]
    labels = ["Até 5k", "5k–10k", "10k–15k", "15k+"]
    df["faixa_receita"] = pd.cut(df["receita_total"], bins=bins, labels=labels, right=False)
    df["faixa_receita"].value_counts().sort_index().plot(
        kind="barh",
        figsize=(7, 4),
        title="Distribuição de Clientes por Faixa de Receita",
        xlabel="Quantidade"
    )
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df_clientes = carregar_clientes()
    resumo_estatistico(df_clientes)
    grafico_clientes_por_estado(df_clientes)
    grafico_receita_por_estado(df_clientes)
    grafico_genero(df_clientes)
    grafico_receita_faixas(df_clientes)
