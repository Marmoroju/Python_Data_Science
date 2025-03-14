#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segnda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f'PARABÉNS! você foi aprovado com a média {media}.')
elif media >= 5.0 and media <= 6.9:
    print(f'Você atingiu a média de {media} e está de recuperação.')
else:
    print(f'Sua média foi de {media} e está reprovado.')