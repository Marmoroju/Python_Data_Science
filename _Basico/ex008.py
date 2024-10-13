#Exercício Python 8: Escreva um programa que leia um valor em metros e
# o exiba convertido em centímetros e milímetros.

medida = float(input('Digite sua medida em metros:'))
cm = medida * 100
mm = medida * 1000
print(f'A meidada convertida em centímetros é {cm} e a medida convertida em milímetros é {mm}')
