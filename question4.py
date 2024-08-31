def calcular_percentuais_por_estado(valores_por_estado):
    total_mensal = sum(valores_por_estado.values())

    percentuais = {}
    for estado, valor in valores_por_estado.items():
        percentual = (valor / total_mensal) * 100
        percentuais[estado] = percentual

    return percentuais

valores_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

percentuais = calcular_percentuais_por_estado(valores_por_estado)

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")


# Saída:
# SP: 37.53%
# RJ: 20.29%
# MG: 16.17%
# ES: 15.03%
# Outros: 10.98%