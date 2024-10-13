#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
anoAtual = date.today().year
idadeMilitar = 18
nasc = int(input('Informe o ano completo de seu nascimento (ex.: 2000): '))
idade = anoAtual - nasc
alistFalta = idadeMilitar - idade
idealAlist = nasc + 18
print(f'Você já completou ou irá completar {idade} anos em {anoAtual}.')
if idade == idadeMilitar:
    print('Parábens, está na hora exata de se alistar!')
    print(f'O ano correto para o seu alistamento será em {idealAlist}')
elif idade > idadeMilitar and idade <= 45:
    print('Vá até a junta militar pois ainda há tempo de de alistar.')
    print(f'O ano correto para o seu alistamento era em {idealAlist}')
elif idade > 45:
    print('Fora do prazo para o alistamento.')
    print(f'O ano correto para o seu alistamento era em {idealAlist}')

elif idade < idadeMilitar:
    print(f'Ainda falta(m) {alistFalta} ano(s) para o alistamento militar!')
    print(f'O ano correto para o seu alistamento será em {idealAlist}')