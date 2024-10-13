#Crie um programa para calcular equações do 1º e 2º grau. Nesse
#programa deve conter ao menos duas funções: calcula_delta()
#e calcula_x(), na qual a primeira função retorna o valor de delta
#de uma equação do segundo grau e a segunda função retorna
#o(s) valor(es) de x da equação. As funções devem receber como
#parâmetros os valores a, b e c de uma equação, cuja expressão
#pode ser dada pela fórmula:
#ax² + bx + c = 0
#Dica: lembre-se de que, se a for igual a zero, a equação é do
#primeiro grau.

def calcula_delta(a, b, c):
    return (b**2) - 4*a*c

def calcula_x(a, b, c):
    if a == 0:
        return -c/b
    else:
        delta = calcula_delta(a, b, c)
        if delta == 0:
            return -b / (2 * a)
        else: 
            x1 = (-b + delta**(1/2)) / (2 * a)
            x2 = (-b - delta**(1/2)) / (2 * a)
            return f'O valor de x1 é {x1}\nO valor de x2 é {x2}'

a = float(input('Informe o valor de a: '))
b = float(input('Informe o valor de b: '))        
c = float(input('Informe o valor de c: '))

print(calcula_x(a, b, c))