#s = str(input('Digite um texto: \n'))
#print(f'O espaço em branco aparece {s.count(' ')} veze(s)')

# LISTAS #
#nota1 = int(input("Insira uma nota: \n"))
#nota2 = int(input("Insira uma nota: \n"))
#nota3 = int(input("Insira uma nota: \n"))
#nota4 = int(input("Insira uma nota: \n"))
#
#notas = [nota1, nota2, nota3, nota4]
#notas.sort()
#print(notas)
#print(min(notas))
#print(max(notas))
#excluir = notas.pop(0)
#print(f'Menor nota {excluir}')
#print(notas[0:])
#
## TUPLAS #
#
#tupla2 = (int(input('Primeiro número: \n')),
#          int(input('Segundo número: \n')),
#          int(input('Terceiro número: \n')),
#          int(input('Quarto número \n'))
#        )
#print(tupla2)
#
#n1 = int(input("Insira um número inteiro: \n"))
#n2 = int(input("Insira um número inteiro: \n"))
#n3 = int(input("Insira um número inteiro: \n"))
#n4 = int(input("Insira um número inteiro: \n"))
#tupla = n1, n2, n3, n4
#print(tupla)
#max = tupla.index(max(tupla))
#print(f'\nO maior número está no índice {max} que é o número {tupla[max]}')
#print(f'Indice 0 = {tupla[0]},\nIndice 1 = {tupla[1]},\nIndice 2 = {tupla[2]},\nIndice 3 = {tupla[3]}\n')
#
#soma = tupla[0] + tupla[1] + tupla[2] + tupla[3]
#soma2 = sum(tupla)
#print(f'A soma de todos os elementos é {soma}\n')
#
#media = sum(tupla) / len(tupla)
#print(f'A média dos valores da tupla é {media}')
#

# DICIONÁRIO

#1 -  Crie um programa que leia o nome, gênero e idade de quatro pessoas, 
#guardando os dados dessas pessoas em um dicionário. No final, mostre: <br>
#a) a maior idade; <br>
#b) a média de idade; <br>
#c) quantas pessoas são do gênero masculino e quantas são do gênero feminino. <br>
#d) qual o percentual de pessoas do gênero feminino.

#listaNomes = ['Joao', 'Maria']; listaGenero = ['M', 'F']; listaIdade = [10, 25]
#
#listaNomes.append(input('Nome: \n'))
#listaGenero.append(input("Genero 'M' ou 'F': \n" ))
#listaIdade.append(int(input('idade: \n')))
#
#
#lista = {"Nome":listaNomes, "Genero": listaGenero, "Idade": listaIdade}
#print(lista)
#
#maiorIdade = max(lista["Idade"])
#print(f'A maior idade é {maiorIdade}')
#
#mediaIdade = sum(lista["Idade"]) / len(lista["Idade"])
#print(f'A média de idades é {mediaIdade}')
#
#generoM = lista["Genero"].count('M')
#print(f'Possui {generoM} pessoa(s) do genero M')
#
#generoF = lista["Genero"].count('F')
#print(f'Possui {generoF} pessoa(s) do genero F')
#
#percF = (generoF / len(lista["Genero"])) * 100
#print(f'O percentual do genero F é {percF}')
#
#percM = (generoM / len(lista["Genero"])) * 100
#print(f'O percentual do genero M é {percM}')


## IF ELSE
#
#perguntas = []
#perguntas.append(str(input("Telefonou para a vítima? Sim ou Não \n")))
#perguntas.append(str(input("Esteve no local do crime? Sim ou Não \n")))
#perguntas.append(str(input("Mora perto da vítima? Sim ou Não \n")))
#perguntas.append(str(input("Devia dinheiro para a vítima? Sim ou Não \n")))
#perguntas.append(str(input("Já trabalhou com a vítima? Sim ou Não \n")))
#
#print(perguntas)
#qtdSim = perguntas.count('Sim')
#
#if (qtdSim == 2):
#    print('Suspeita')
#elif (qtdSim == 3 or qtdSim == 4):
#    print('Cumplice')
#elif (qtdSim == 5):
#    print('Assassino(a)')
#else:
#    print('Inocente')    


from random import randint

numerosPares = []
numerosImpares = []
quantidadePares = 0
quantidadeImpares = 0

for k in range(1000):
    numero = randint(1,1000)
    if numero % 2 == 0:
        numerosPares.append(numero)
        quantidadePares += 1
    else:
        numerosImpares.append(numero)        
        quantidadeImpares += 1
else:
    print(f'São {quantidadePares} números pares e {quantidadeImpares} números ímpares')        

