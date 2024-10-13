#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador pensar
print('-=-' * 18)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 18)
jogador = int(input('Em que número eu pensei?')) #jogador tenta adivinhar
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns, você venceu!')
else:
    print(f'Você perdeu! O número que eu pensei foi {computador} e você {jogador}')


