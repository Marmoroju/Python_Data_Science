#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmPercorrido = int(input('Qual a quantidade de KM percorrido?'))
diaAlugado = int(input('Por quantos dias o carro foi alugado?'))
diaria = diaAlugado * 60
kmRodado = kmPercorrido * 0.15
print(f'O carro foi alugado por {diaAlugado} dia(s), foram percorridos nesse período {kmPercorrido}KM(s).')
print(f'O valor da diária será R$ {diaria :.2f}.')
print(f'o valor do KM percorrido será R$ {kmRodado :.2f}.')
print(f'O total a pagar será: R$ {diaria + kmRodado :.2f}.')