# 🧮 Simulador de Banco de Dados de Clientes (Python)

Este projeto simula uma base de dados corporativa de clientes utilizando **Python** e **JSON** como fonte primária.  
O objetivo é permitir experimentos e análises de dados de forma local — sem depender de banco de dados real — ideal para **testes, aprendizado de data analytics e prototipagem de ETL**.

---

## 🚀 Estrutura do Projeto

/empresa_dados/
│
├── clientes.json # Base simulada com ~200 clientes
├── analise_cliente.py # Script de análise dos dados
└── utils/
├── init.py
└── gerador_clientes.py # Gerador automático de clientes fake


---

## 🎯 Objetivos

- Simular um banco de dados de clientes realista.  
- Executar análises básicas de negócio:
  - Média de idade e receita.
  - Clientes ativos e VIP.
  - Distribuição por estado e gênero.
- Servir de base para estudos de **Python Data Analysis**, **pandas**, **ETL**, **dashboards**, etc.

---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/GeovaneParedes/simulador_clientes.git
cd simulador-clientes


2️⃣ Criar ambiente virtual (recomendado)

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# ou
.venv\Scripts\activate      # Windows

3️⃣ Instalar dependências

pip install -r requirements.txt

Dependência principal:

faker

🧩 Uso
🔹 Gerar base de clientes

O script abaixo cria um arquivo clientes.json com 200 clientes aleatórios.

python utils/gerador_clientes.py

Exemplo de cliente gerado:

{
  "id": 1,
  "nome": "Carlos Oliveira",
  "idade": 34,
  "email": "carlos.oliveira@example.com",
  "telefone": "+55 11 91234-5678",
  "estado": "SP",
  "cidade": "São Paulo",
  "genero": "M",
  "data_cadastro": "2023-07-21",
  "receita_total": 12500.75,
  "ativo": true
}

🔹 Executar análise

python analise_cliente.py

Saída esperada (exemplo):

Total de clientes: 200
Ativos: 152 (76.0%)
Média de idade: 39.7
Receita total: R$ 1,789,540.82
Média de receita por cliente: R$ 8,947.70
Clientes VIP (>R$ 15.000): 35
Distribuição por estado: {'SP': 38, 'RJ': 26, 'MG': 24, ...}
Distribuição por gênero: {'M': 96, 'F': 104}

📊 Próximos Passos

Implementar versão com pandas para análise mais rica.
Adicionar visualizações gráficas (matplotlib / plotly).
Criar pipeline de atualização automática dos dados.
Exportar relatórios em CSV, Excel ou Dashboard Web.

🧠 Conceitos Envolvidos

Geração sintética de dados com Faker.

Manipulação de listas e dicionários em Python.

Leitura/escrita de JSON com encoding UTF-8.

Estatísticas descritivas (média, contagem, soma).

Organização modular e boas práticas de código.

🧩 Tecnologias

Stack	Versão mínima	Uso principal
Python	3.11	Linguagem principal
Faker	≥ 25.0	Geração de dados falsos


📜 Licença

Este projeto é de uso livre para fins educacionais e de experimentação.
Sinta-se à vontade para forkar, melhorar e documentar suas análises.

👨‍💻 Autor

@DevGege
Programador Sênior • Software & DevOps

Código limpo, modular e sem gambiarras.
"Dados bem estruturados contam boas histórias."
