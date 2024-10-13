#Lemos o código da seguinte forma: “para a variável var que
#percorrerá valores dentro de um intervalo, faça...”.

#for x in [5, 10, 15]:
#    print(x)

#tabuada = int(input('Escolha o valor da tabuada: '))
#for x in range(11):
#    print(f'{tabuada} x {x} = {tabuada * x}')

#for num in range(1,11):
#    if num%2 == 0:
#        print(num)

limite = int(input('Informe o número'))
for num in range(1, limite + 1):
    if num%2 == 0:
        print(num)