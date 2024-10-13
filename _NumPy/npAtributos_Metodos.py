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
print('vetor2.shape e matriz1 - Retorna o formato de um Array')
print(vetor2.shape)
print(matriz1.shape)
print('\n')

#Retorna o tipo de dada de um array
print('Retorna o tipo de dada de um array')
print(matriz2.dtype)
print('\n')

#Retorna a quantidade de elementos de um array
print('Retorna a quantidade de elementos de um array')
print(matriz2)
print(matriz2.size)
print('\n')

#Retorna a soma dos elementos de um array
print('matriz2 - Retorna a soma dos elementos de um array')
print(matriz2.sum())
print('\n')

#Retorna a soma de cada COLUNA
print(matriz1)
print('Retorna a soma de cada COLUNA')
print(matriz1.sum(axis = 0))
print('Retorna a soma de cada LINHA')
print(matriz1.sum(axis = 1))
print('\n')

#Retorna a soma acumulada dos elementos de um array
print('Retorna a soma acumulada dos elementos de um array')
print(vetor2)
print(vetor2.cumsum())
print('\n')

#Retorna a média dos elementos de um array
print('Retorna a média dos elementos de um array - .mean()')
print(vetor2)
print(vetor2.mean())

#Retorna a média dos elementos de um array
print('Retorna a média dos elementos de um array - np.median()')
print(vetor2)
print(np.median(vetor2))
print('\n')

#Retorna a variancia dos elementos de um array
# A variância indica a distância que os valores se encontram em relação a média
print('Retorna a variancia dos elementos de um array')
print(vetor2)
print(vetor2.var())
print('\n')

#Retorna o desvio padrão dos elementos de um array
#O desvio padrão é a raiz quadrada da variância
print(vetor2)
print(vetor2.std())
print('\n')

#Retorna o valor máximo e mínimo dos elementos de um array
print('Retorna o valor máximo e mínimo dos elementos de um array')
print(vetor2)
print(f'O maior valor é {vetor2.max()} e o menor valor é {vetor2.min()}')
print('\n')

# Criando um array com valores sequenciais
