#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle
alunoUm = str(input('Nome do primeiro aluno: '))
alunoDois = str(input('Nome do segundo aluno: '))
alunoTres = str(input('Nome do terceiro aluno: '))
alunoQuatro = str(input('Nome do quarto aluno: '))
lista = [alunoUm, alunoDois, alunoTres, alunoQuatro]
shuffle(lista)
print(f'A ordem de apresentação é: {lista}')