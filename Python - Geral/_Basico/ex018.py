#Exercício Python 18: Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, tan, cos, radians
angulo = float(input('Digite o angulo que você deseja:  '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem o SENO de {seno :.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {cosseno :.2f}')
print(f'O angulo de {angulo} tem a TANGENTE de {tangente :.2f} ')