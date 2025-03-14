# Exercício 04
# Faça um programa que faça algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ela.

n = input('Digite algo:')
print('O tipo primitivo da variável é: {}', type(n))
print('N é alpha? {}', n.isalpha())
print('N é numérico? {}', n.isnumeric())
print('N é decimal? {}', n.isdecimal())
print('N tem espaço?', n.isspace())
