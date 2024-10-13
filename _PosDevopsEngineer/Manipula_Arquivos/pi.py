from random import randint
ran = randint(0,10)

num = int(input("Digite um número: "))
cont = 1
if (num == ran):
    print("Parabéns, você acertou de primeira!")
    print(f'O número sorteado foi: {ran}')
else:
    while (num != ran):
        cont += 1
        num = int(input('Que pena, você digitou um número errado. Digite outro número novamente: '))
        if (num == ran):
            print('Parabéns!!! Você Acertou!')
            print(f'O número sorteado foi: {ran}')
            print(f'Você tentou {cont} vezes até acertar.')

     