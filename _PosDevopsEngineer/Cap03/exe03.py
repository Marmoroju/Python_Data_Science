#Escolha um número inteiro e armazene-o em uma variável. Nesse
#mesmo programa, solicite ao usuário para tentar adivinhar qual
#é o valor cadastrado. O programa só deve finalizar quando o
#usuário acertar o número. Esse software também deverá mostrar
#a quantidade de vezes que o usuário errou o palpite.

numx = 18
erros = 0
num1 = int(input('Adivinhe o número armazenado: '))
while (num1 != numx):        
        erros += 1
        num1 = int(input('Tente adivinhar novamente: '))
        print(f'O número {num1} não é o correto.')     

print(f'\nAcertou! O número armazenado é {numx}')
print(f'Você teve {erros} Tentativas até acertar.\n')
   

 


