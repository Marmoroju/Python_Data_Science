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
print('Criando um array com valores sequenciais - np.arange()')
vetor4 = np.arange(10)
print(vetor4)
print('\n')

# Criando um array de duas dimensões com valores sequenciais
print('Criando um array de duas dimensões com valores sequenciais')
matriz3 = np.arange(12).reshape(3, 4)
print(matriz3)
print('\n')

# Mudando o formato do array
print('Mudando o formato do array')
matriz4 = matriz3.reshape(6, 2)
print(matriz4)
print('\n')

# Mudando o formato do array informando apeas a quantidade de linhas
print('Mudando o formato do array informando apeas a quantidade de linhas')
matriz5 = matriz3.reshape(2, -1)
print(matriz5)
print('\n')

# Mudando o formato do array informando apeas a quantidade de Colunas
print('Mudando o formato do array informando apeas a quantidade de Colunas')
matriz6 = matriz3.reshape(-1, 3)
print(matriz6)
print('\n')

# Converte uma matriz em um vetor
print('Converte uma matriz em um vetor')
matriz7 = matriz3.flatten()
print(matriz7)
print('\n')

# Criando um vetor com números aleatórios
# [start, end, size]
print('Criando um vetor com números aleatórios')
vetor5 = np.random.randint(5, 100, 8)
print(vetor5)
print('\n')

# Criando um array de duas dimensões com valores aleatórios
print('Criando um array de duas dimensões com valores aleatórios')
matriz8 = np.random.randint(1, 1000, 15).reshape(5, 3)
print(matriz8)
print('\n')

# Criando um vetor especificando a quantidade de elementos de dentro de um intervalo
# O último elemento é inclusivo
print('Criando um vetor especificando a quantidade de elementos de dentro de um intervalo')
vetor9 = np.linspace(1, 100, 20)
print(vetor9)
print('\n')

# Criando uma matriz de zeros (Tuplas)
print('Criando uma matriz de zeros - Tuplas')
matrizZeros = np.zeros((4, 6))
print(matrizZeros)
print('\n')

# Criando uma matriz com todos os elementos iguais a 1
print('Criando uma matriz com todos os elementos iguais a 1')
matrizUm = np.ones([4, 4])
print(matrizUm)
print('\n')

# Contar valores únicos no array NumPy
print('Contar valores únicos no array NumPy')
matrizUnique = np.unique(matrizZeros, return_counts=True)
print(matrizUnique)
print('\n')

# Inserir uma nova linha na matriz
print('matriz3')
print(matriz3)
print('Inserindo uma nova linha na matriz3')
print('axis = 0 insere uma nova linha. Neste caso inseriu os valores 1, 2, 3, 4')
print('Se a linha possui 4 elementos(colunas), então devem ser informados aquela quantidade de elementos')
matrizLinha = np.append(matriz3, [[1, 2, 3, 4]], axis=0)
print(matrizLinha)
print('\n')


# Inserir uma nova coluna na matriz
print('matriz3')
print(matriz3)
print('Inserindo uma nova coluna na matriz3')
print('axis = 1 insere uma nova Coluna. Neste caso inseriu os valores 1, 2 ,3')
print('Se a coluna possui 4 elementos(linhas), então devem ser informados aquela quantidade de elementos')
print('Com a diferença que cada elemento deve estar dentro de um colchete [1], [2], [3]')
matrizColuna = np.append(matriz3, [[1], [2], [3]], axis=1)
print(matrizColuna)
print('\n')
##### OPERAÇÕES BÁSICAS #####
print('### OPERAÇÕES BÁSICAS ###')
# Criando doi arrays com uma dimensão
v1 = np.array([20, 30 ,40 , 50])
v2 = np.arange(4)
print(f'Array v1 = {v1}')
print(f'Array v2 = {v2}')
print('\n')

# Soma dos arrays v1 + v2
print('Soma dos arrays v1 + v2')
print(v1 + v2)
print('O Elemento 0 do v1 soma-se ao elemento 0 do v2')
print('O Elemento 1 do v1 soma-se ao elemento 1 do v2')
print('E assim sucessivamente')
print('Na SUBTRAÇÃO v1 - v2 ocorre da mesma maneira')
print('Na COMPARAÇÃO v1 == v2 ocorre da mesma maneira')
print('Na MULTIPLICAÇÃO v1 * v2 ocorre da mesma maneira')
print('\n')

# Potencialização
print('Potencialização do v2 por 2')
print(v2)
print(v2**2)
print('Cada elemento é potencializado por 2')

# Multiplicação de matrizes pelo método .dot
n1 = np.array([[5, 2],
               [0, 1]])

n2 = np.array([[2, 0],
               [3, 4]])

print(f'A matriz n1 = \n{n1}')
print(f'A matriz n2 = \n{n2}')
print('O resltado da multiplicação das matrizes é')
multiplicaMatriz = n1.dot(n2)
print(multiplicaMatriz)
