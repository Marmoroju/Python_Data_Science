#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.



valorCasa = int(input('Qual o valor da casa?'))
salario = int(input('Qual é o seu salário atual?'))
anosCasa = int(input('Em quantos anos deseja pagar a casa?'))


#calcula quantos reais pode pagar por mês
salarioPercent = ((salario / 100) * 30)
print('-=-' * 30)
#calcula o valor da prestação
prestCasa = valorCasa / (anosCasa * 12)
podePagar = (valorCasa / (salarioPercent * 12))
x = valorCasa / (anosCasa * 12)
if prestCasa < salarioPercent:
    print('Parabéns, você poderá financiar sua casa no tempo desejado.')
    print(f'Com 30% do seu salário, você poderá pagar as prestações até o valor de R$ {salarioPercent} reais.')
    print(f'Durante esse tempo a prestação da casa será de R$ {prestCasa:.2f} reais durante {anosCasa} anos.')
elif prestCasa > salarioPercent:
    print('Infelizmente você não poderá financiar a casa no tempo desejado.')
    print(f'Nesse tempo de {anosCasa} anos que deseja financiar as prestações mínimas devem ser de R$ {x:.2f} reais.')
    print(f'Com 30% do seu salário irá conseguir pagar somente em {podePagar:.0f} anos com parcelas de R$ {salarioPercent:.2f} reais.')
print('-=-' * 30)





