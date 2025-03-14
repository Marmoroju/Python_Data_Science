#Exercício Python 14: Escreva um programa que converta uma temperatura
# digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Graus Celsius:'))
fahrenheit = (celsius * 1.8) + 32
print(f'A temperatura de {celsius :.1f}ºC convertida para Fahrenheit é de {fahrenheit :.1f}ºF.')
