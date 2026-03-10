import math
#leituras
assinantes = int(input('Digite a qtd de assinates:'))
mensalidade = float(input('Digite o valor da mensalidade:'))
taxa = float(input('Digite a taxa de crescimento mensal %:'))/100
meses = int(input('digite aqtd de meses de projeção:'))
#processamento
assinantes_finais = assinantes * math.pow((1 + taxa), meses)
receita_final = assinantes_finais * mensalidade
#saida
print(f'assinantes estimados: {assinantes_finais:.0f}')
print(f'Receita estimada: R${receita_final:.2f}')