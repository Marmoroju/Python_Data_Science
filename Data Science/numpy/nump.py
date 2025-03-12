import numpy as np

#criando um array com uma dimensão (com um axis) a partir de uma lista
vetor1 = np.array([2, 3, 4, 5, 6, 7, 8, 9])
print(f'Axis a partir de uma lista \n{vetor1}\n')

#Criando um array com uma dimenrsão (com um axis) a partir de uma tupla
vetor2 = np.array((10, 11, 12, 13, 14))
print(f'Axis a partir de uma tupla \n{vetor2}\n')

#Criando um array com duas dimensões (Dois axis), sendo 2 linhas
#e 3 colunas utilizando uma lista de listas
#Cada Lista é uma Linha da matriz e a quantidade de elementos de uma lista, 
#define o número de colunas

#O primeiro Axis (linhas) tem tamanho 2
#O segundo Axis (colunas) tem tamanho 3
matriz1 = np.array([[10, 20, 30], [40, 50, 60]])
print(f'Matriz de duas linhas e três colunas\n{matriz1}\n')

#O primeiro Axis (linhas) tem tamanho 3
#O segundo Axis (colunas) tem tamanho 2
matriz2 = np.array([(15, 25), (35, 45), (55, 65)])
print(f'Matriz de três linhas e duas colunas\n{matriz2}\n')

# SLICING #
print(f'Foi recuperado o índice 0 até o índice 3 do array vetor1\n{vetor1[0:3]}')

#O fatiamento em matrizes possui um índice por dimensão
print(f'Foi recuperado o índice 0 da linha 1 da matriz matriz1\n{matriz1[0,0]}')

#Recuperando o elemento que está na segunda linha e na terceira coluna
#matriz[linha, coluna]
#matriz[1(linha),2(coluna)] -- inicia-se por 0
print(f'Foi recuperado da linha 1 (0, 1) e coluna 2 (0, 1, 2) da matriz matriz1\n{matriz1[1,2]}')

#Alterando o elemento que está na na segunda linha e terceira coluna
matriz1[1,2] = 88
print(f'O elemento da terceira coluna e segunda linha foi alterado para 88\n{matriz1}\n')
#print(f'Foi recuperado da linha 1 (0, 1) e coluna 2 (0, 1, 2) da matriz matriz1\n{matriz1[1,2]}')

#Recuperando todos os indices da primeira e terceira coluna da matriz1
#matriz[: (recupera todas as linhas), 1:3(recupera a 1ª e 3ª coluna )]
print(matriz1[:, 1:3])

# MÉTODOS E ATRIBUTOS DE UM ARRAY #
print(f'\nMatriz matriz1 possui {matriz1.ndim} dimensões, isto é {matriz1.ndim} linhas ou {matriz1.ndim} axis.\n')

#Imprimir o formato da matriz
print(f'Portanto, o formato da matriz1 é {matriz1.shape}\n')



