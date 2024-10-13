# Faça um programa que solicite ao usuário dois números e
# informe qual dos dois números é maior ou se ambos são iguais.

num1 = int(input('Digite um número qualquer\n'))
num2 = int(input('Digite um outro número qualquer\n'))

if (num1 > num2):
    print(f'O {num1} é maior do que {num2}')
elif (num1 == num2):
    print('Ambos os números digitados são iguais')
else:
    (num2 > num1)       
    print(f'O {num2} é maior do que {num1}')
