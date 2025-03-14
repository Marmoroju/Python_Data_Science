#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número: '))
baseconv = int(input('Digite 1 para converter em Binário, 2 para Octal ou 3 para Hexadecimal: '))
if baseconv == 1:
    print(f'Convertendo o número {num} para base binária o resultado é: {bin(num)[2:]}')
elif baseconv == 2:
    print(f'Convertendo o número {num} para base Octadecimal o resultado é: {oct(num)[2:]}')
elif baseconv == 3:
    print(f'Convertendo o número {num} para base Hexadecimal o resultado é: {hex(num)[2:]}')
else:
    print('Número errado, tente outra vez!')
