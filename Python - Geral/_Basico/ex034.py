#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e
# calcule o valor do seu aumento. Para salários superiores a R$1250,00,
# calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Quantos é o seu salário?'))
dez = ((salario / 100) * 10) + salario
quinze = ((salario / 100) * 15) + salario
if salario > 1250:
    print(f'O seu salário atual é R$ {salario:.2f} reais. Receberá um aumento de 10% e receberá agora R$ {dez:.2f} reais.')
else:
    print(f'O seu salário atual é R$ {salario:.2f} reais. Receberá um aumento de 15% e receberá agora R$ {quinze:.2f} reais.')