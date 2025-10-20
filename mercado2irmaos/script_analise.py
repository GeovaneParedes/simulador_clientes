#!/usr/bin/env python3
import json


# Carrega o JSON como uma lista de dicionários
with open("bdados_venda.json", "r", encoding="utf-8") as arquivo_json:
    vendas = json.load(arquivo_json)

# Fatiamento (slicing)
print(f"Total de vendas: {len(vendas)}")

# 1. As primeiras 3 vendas
primeiras_tres = vendas[:3]
print("\nPrimeiras 3 vendas:")
for venda in primeiras_tres:
    print(venda['produtos'], end='\n')
# Para não poluir, imprimo apenas o ID

# 2. A última venda (pode ser usado para fatiamento ou indexação)
ultima_venda = vendas[-1]
print("\nÚltima venda (ID):", ultima_venda['id_venda'],
      "- Produtos:", ultima_venda['produtos'], end='\n')

# 3. Vendas do segundo ao quarto (índices 1, 2 e 3)
do_segundo_ao_quarto = vendas[1:4]
print("\nVendas do segundo ao quarto (IDs):")
for venda in do_segundo_ao_quarto:
   print(venda['id_venda'])

# 4. Fatiamento com passo (a cada duas vendas)
a_cada_duas = vendas[::2]
print("\nVendas a cada duas (IDs):")
for venda in a_cada_duas:
    print(venda['id_venda'])

# 5. Total de Vendas
print("\nTotal de vendas carregadas:", len(vendas))
soma_total = 0.0
# 6. Iterar e acumular (usando for loop com incremento)
for venda in vendas:
    soma_total += venda['valor_total']# O incremento é feito com o operador +=
    
# 7. Imprimir o resultado
print("Vendas individuais (para conferência):")
for venda in vendas:
    print(f"ID {venda['id_venda']}: R$ {venda['valor_total']:.2f}", end='\n')
print("-" * 20)
print(f"Total de vendas (soma acumulada): R$ {soma_total:.2f}")