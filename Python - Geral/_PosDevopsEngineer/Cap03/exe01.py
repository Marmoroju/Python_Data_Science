#Uma equação do segundo grau é dada pela seguinte expressão:
#ax² + bx + c = 0
#Em que a, b e c são constantes e a deve ser diferente de 0. Pela
#fórmula de Bhaskara, a solução dessa equação é dada pela fórmula:
#Sendo Δ = b² – 4ac.

#Crie um programa em Python que calcule as raízes reais de
#x de uma equação de segundo grau, ou seja, somente serão
#impressos valores cujo valor de Δ seja maior ou igual a 0. O usuário
#deverá fornecer os valores das constantes a, b e c. Sempre
#que o valor de a for igual a 0, o programa deve solicitar que o
#usuário informe um novo valor diferente de 0.

a = float(input('Digite o valor de a: '))
while (a == 0):
    a = float(input("O valor de 'a' não pode ser 0.\nDigite novamente: "))
b = float(input("Digite o valor de b: "))    
c = float(input('Digite o valor de c: '))

delta = b**2 - 4*a*c
print(f'Delta = {delta}')
if (delta < 0):
    print('Esta equação não possui raízes reais.')
elif (delta == 0):
    x = -b/(2*a)
    print(f'x = {x}')
else:
    x1 = (-b + (delta)**(1/2))/(2*a)
    x2 = (-b - (delta)**(1/2))/(2*a)
    print(f'x1 = {x1}\n'
          f'x2 = {x2}\n')