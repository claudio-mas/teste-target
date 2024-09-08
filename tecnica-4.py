# Técnica 4)
# Linguagem: Python

faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}
total_faturamento = sum(faturamento_estados.values())

percentuais = {}
for estado, faturamento in faturamento_estados.items():
    percentual = (faturamento / total_faturamento) * 100
    percentuais[estado] = percentual
    print(f"Percentual de representação de {estado}: {percentual:.2f}%")
