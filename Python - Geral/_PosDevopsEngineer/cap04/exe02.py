#Crie um programa que pergunte ao usuário de qual forma
#geométrica ele deseja calcular a área (círculo, retângulo ou
#triângulo) e imprima o valor da área ao receber as dimensões da
#figura. Organize o código em funções com parâmetros e retornos.
#Dica: considere pi = 3,14.

def calcula_area_retangulo(base, altura):
    return base * altura

def calcula_area_triangulo(base, altura):
    return (base * altura) / 2

def calcula_area_circulo(raio):
    return 3.14 * (r**2)

while True:
    forma = input("Qual forma geométrica deseja calcular a área?\n"
                  "[r] retangulo\n"
                  "[t] triângulo\n"
                  "[c] círculo\n"
                  "[s] sair\n")
    if forma == "r":
        b = float(input("Informe a base do retângulo: "))
        a = float(input("Informe altura do retângulo: "))
        print(f'Área do retângulo {calcula_area_retangulo(b,a)}')
        break
    elif forma == "t":
        b = float(input("Informe a base do triângulo: "))
        a = float(input("Informe a altura do triângulo: "))
        print(f'Área do triângulo {calcula_area_triangulo(b,a)}')
        break
    elif forma == "c":
        r = float(input("Informe o raio do círculo: "))
        print(f'Área do círculo {calcula_area_circulo(r)}')
        break
    elif forma == "s":
        break # sai do loop e encerra o programa
    else:
        print("Opção inexistente")




