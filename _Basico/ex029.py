#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velCarro = int(input('O carro estava a que velocidade (Km/h)?'))
if velCarro > 80:
    multa = (velCarro - 80) * 7
    print(f'Você foi multado por ultrapassar os 80 Km/h. Velocidade atingida {velCarro} km/h. ')
    print('A multa será de R$ 7,00 por cada Km acima do limite')
    print(f'A multa aplicada será de R$ {multa} reais.')
else:
    print(f'{velCarro} Km/h, velocidade dentro do limite permitido.')