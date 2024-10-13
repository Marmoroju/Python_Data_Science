#Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.

#considere US$ 1,00 = R$ 5,60 em 05/11/2021
#considere EUR 1,00 = R$ 6.45 em 05/11/2021

dinheiro = float(input('Quanto de dinheiro você tem na carteira? R$'))
convertDolar = dinheiro / 5.60
convertEuro = dinheiro / 6.45
print(f'Você pode comprar {convertDolar :.2f} US$.')
print(f'Você pode comprar {convertEuro :.2f} EUR$')
