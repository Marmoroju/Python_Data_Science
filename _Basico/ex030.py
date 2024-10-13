#Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número inteiro para saber se é PAR ou ÍMPAR:'))
resultado = num % 2
if resultado == 1:
    print(f'O número {num} é ímpar.')
else:
    print(f'O número {num} é par.')
