#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

#a raiz quadrada é representada pela hipotenuza
'''from math import sqrt, trunc
catOposto = float(input('Digite o valor do cateto oposto:'))
catAdjacente = float(input('digite o valor do cateto adjacente'))
hipotenusa = sqrt((catOposto ** 2) + (catAdjacente ** 2))
print(f'O valor do Cateto Oposto é {catOposto ** 2} e o Cateto Adjacente é {catAdjacente ** 2}. O valor da Hipotenusa é {trunc(hipotenusa)}')'''

from math import hypot, trunc
catOp = float(input('Digite o valor do cateto oposto.'))
catadj = float(input('Digite o valor do cateto adjacente.'))
hipo = hypot(catadj, catOp)
print(f'O valor da hipotenusa é {trunc(hipo)}')