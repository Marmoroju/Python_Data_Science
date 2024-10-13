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

#Verifica a quantidade de dimensões de um array
print('vetor2.ndim - Verifica a quantidade de dimensões de um array')
print(vetor2)
print(vetor2.ndim)
print('\n')

#Verifica o formato e quantidade de elementos de um Array
print('vetor2.shape - e matriz1 Verifica o formato e quantidade de elementos de um Array')
print(vetor2.shape)
print(matriz1.shape)