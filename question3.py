# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def carregar_faturamento_de_arquivo(arquivo_nome):
    with open(arquivo_nome, 'r') as arquivo:
        dados = json.load(arquivo)
        return dados.get("faturamento_diario", [])

def calcular_faturamento(vetor_faturamento):
    dias_com_faturamento = [valor for valor in vetor_faturamento if valor > 0]

    menor_valor = min(dias_com_faturamento)
    maior_valor = max(dias_com_faturamento)

    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_media

faturamento_diario = carregar_faturamento_de_arquivo("faturamento.json")

menor, maior, acima_media = calcular_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {acima_media}")

# Saída: 
# Menor valor de faturamento: R$100.00
# Maior valor de faturamento: R$250.00
# Dias com faturamento acima da média: 4