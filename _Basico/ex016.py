# Crie um programa que leia um número REAL qualquer pelo teclado e mostre
# na tela a sua proporção inteira

from math import trunc

num = float(input('Digite um número qualquer:'))
numInteiro = trunc(num)
print(f'A porção inteira do número digitado é {numInteiro}.')
