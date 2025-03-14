import numpy as np
 
# Criando um array com uma dimensão (1 axis) a partir de uma lista
# axis = dimensão
vetor1 = np.array([2, 3, 4, 5, 6, 7, 8, 9])
print('Array com 1 axis (axis = dimensão)')
print(vetor1)

# Criando um array de 1 axis a partir de uma tupla
vetor2 = np.array((10, 11, 12, 13, 14, 15))
print('array de 1 axis a partir de uma tupla')
print(vetor2) 

# Array com 2 axis (Lista de lista)
# Primeiro axis (linhas) tem tamanho 2
# Segundo axis (colunas) tem tamanho 3

matriz1 = np.array([[10, 20, 30], [40, 50, 60]])
print('Array com 2 axis e três dimensões')
print(matriz1)

#Array com duas dimensões (2 axis), sendo 3 linhas e duas colunas utilizando uma lista de tuplas
matriz2 = np.array([(15, 25), (35, 45), (55, 65)])
print('Tupla com 2 axis e duas dimensõs')
print(matriz2)