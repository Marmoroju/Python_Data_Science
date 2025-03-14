#contador = 0
#while contador <= 10:
#    print(contador)
#    contador += 1

num = int(input("Digite um número inteiro e positivo: \n"))

n = num
resultado = num

while n > 1:
    resultado *= n - 1
    n -= 1
else:
    if num  == 0 or num == 1:
        print(f'O fatorial de {num} é 1\n')
    else:
        print(f'O fatorial de {num} é {resultado}')    
