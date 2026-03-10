import random
cotacao = float(input('Cotacao atual do dolar:'))
variacao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1 + variacao)
print(f'variacao simulada: {variacao:.3%}')
print(f'nova cotacao: {nova_cotacao:.2f}')