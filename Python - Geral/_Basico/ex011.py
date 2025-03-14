#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Qual a altura da parede em metros?'))
largura = float(input('Qual a largura da parede em metros?'))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem {area :.1f} metro(s)m² quadrado(s). Para pintá-la será preciso {tinta :.1f} litro(s) de tinta.')