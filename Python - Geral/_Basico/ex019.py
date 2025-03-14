# Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice

alunoUm = str(input('Qual o nome do primeiro aluno? '))
alunoDois = str(input('Qual o nome do segundo aluno? '))
alunoTres = str(input('Qual o nome do terceiro aluno? '))
alunoQuatro = str(input('Qual o nome do quarto aluno? '))
lista = [alunoUm, alunoDois, alunoTres, alunoQuatro]
print(f'o aluno sorteado foi {choice(lista)}')
