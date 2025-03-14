#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
# com 5% de desconto.

produto = float(input('Qual o valor do produto? R$'))
desconto = int(input('Qual o valor do desconto?'))
comDesconto = produto - ((produto / 100) * desconto)
print(f'O valor do produto é R$ {produto :.2f}. Com desconto de {desconto}% ele sai a R$ {comDesconto :.2f}!')
