#O programa deve gerar uma lista com números aleatórios da seguinte forma:
# receber um número inicial inteiro;
# receber um número final inteiro;
# receber a quantidade de números a serem gerados;
# gerar a lista dentro do intervalo inicial e final com a quantidade de números solicitada

import random

numInicial = int(input('Digite o número inicial: '))
numFinal = int(input('Digite o número final: '))
gerar = int(input('Digite a quantidade a ser gerada: '))
geradorLista = random.sample(range(numInicial, numFinal), gerar)
print(geradorLista)



