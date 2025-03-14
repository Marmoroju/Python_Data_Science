#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 parta viagens mais longas.

dist = int(input('Qual a distância em KM da viagem?'))
if dist <= 200:
    menor = dist * 0.50
    print(f'A distancia será de {dist} KMs e o valor a ser cobrado será de R$ {menor:.2f} reais.')
else:
    maior = dist * 0.45
    print(f'A distância será de {dist} KMs e o valor a ser cobrado será de R$ {maior:.2f} reais')

