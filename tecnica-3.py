# Técnica 3)
# Linguagem: Python

import json


with open('dados.json', 'r') as file:
    dados = json.load(file)


faturamentos = [dia['valor'] for dia in dados if dia['valor'] > 0]

menor_faturamento = min(faturamentos)
menor_faturamento = f"{menor_faturamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
maior_faturamento = max(faturamentos)
maior_faturamento = f"{maior_faturamento:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

media_mensal = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")
