import numpy as np

# Criando um array com uma dimensão (1 axis) a partir de uma lista
# axis = dimensão
vetor1 = np.array([2, 3, 4, 5, 6, 7, 8, 9])

# Criando um array de 1 axis a partir de uma tupla
vetor2 = np.array((10, 11, 12, 13, 14, 15))

# Array com 2 axis (Lista de lista)
# Primeiro axis (linhas) tem tamanho 2
# Segundo axis (colunas) tem tamanho 3

matriz1 = np.array([[10, 20, 30], [40, 50, 60]])

#Array com duas dimensões (2 axis), sendo 3 linhas e duas colunas utilizando uma lista de tuplas
matriz2 = np.array([(15, 25), (35, 45), (55, 65)])

#Imprime primeiro elemento do array
print('Primeiro vetor')
print(vetor1[0])
print('\n')

#Imprime os elementos da posição 0 até a posição 3
print('Imprime os elementos da posição 0 até a posição 3')
print(vetor1[0:3])
print('\n')

#Imprime o elemento que está na primeira linha e na primeira coluna
#Imprime os elementos da posição 0 até a posição 3
print('Imprime o elemento que está na primeira linha e na primeira coluna')
print(matriz1[0, 0])
print('\n')


#Alterar valor do elemento que está na primeira linha e segunda coluna
print('Alterar valor do elemento que está na primeira linha e segunda coluna')
print(matriz1)
matriz1[0, 1] = 88
print('\n')
print(matriz1)
print('\n')

#Recuperando as linhas 0, 1 e 2 da primeira coluna
print('Conteúdo da matriz2')
print(matriz2)
print('Recuperando as linhas 0, 1 e 2 da primeira coluna')
print(matriz2[0:3, 0])
print('[0, 0] Primeiro [0] refere-se aos índices da linhas da matriz | Segundo [0] refere-se aos índices da colunas da matriz')
print('\n')

#Uma forma de recuperar todas as linhas é atribuindo somente o :
print('Conteúdo da matriz2')
print(matriz2)
print('Recuperando as linhas 0, 1 e 2 da primeira coluna através do :')
print(matriz2[:, 0])
