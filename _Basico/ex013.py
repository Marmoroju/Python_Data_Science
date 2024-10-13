#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

salarioAtual = float(input('Digite o valor do seu salário atual. R$'))
aumento = int(input('Digite quantos porcento teve de aumento: %'))
comAumento = salarioAtual + ((salarioAtual / 100) * aumento)
print(f'O seu salário atual é de R$ {salarioAtual :.2f}. Com {aumento}% de aumento, você irá receber R${comAumento :.2f}.')
print(f'Com isso você recebeu um aumento de R$ {comAumento - salarioAtual :.2f}')