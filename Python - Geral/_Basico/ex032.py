#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Digite um ano qualquer ou digíte 0 para o saber se o ano atual é Bissexto:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano %400 ==0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é BISSEXTO.')