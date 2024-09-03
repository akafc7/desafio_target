# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
import os

def carregar_faturamento_de_arquivo(arquivo_nome):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_absoluto = os.path.join(diretorio_atual, arquivo_nome)

    with open(caminho_absoluto, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    return dados

def calcular_faturamento(dados_faturamento):
    dias_com_faturamento = [dia['valor'] for dia in dados_faturamento if dia['valor'] > 0]

    menor_valor = min(dias_com_faturamento)
    maior_valor = max(dias_com_faturamento)

    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_media

arquivo_nome = "dados.json"

faturamento_diario = carregar_faturamento_de_arquivo(arquivo_nome)

menor, maior, acima_media = calcular_faturamento(faturamento_diario)

print(f"Menor valor de faturamento: R${menor:.2f}")
print(f"Maior valor de faturamento: R${maior:.2f}")
print(f"Dias com faturamento acima da média: {acima_media}")

# Saída:
# Menor valor de faturamento: R$373.78
# Maior valor de faturamento: R$48924.24
# Dias com faturamento acima da média: 10