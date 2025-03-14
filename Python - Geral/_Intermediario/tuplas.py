## TUPLAS NÃO PODEM SER MODIFICADAS ##
## QUANDO HOUVER APENAS UM ELEMENTO SERÁ UTILIZADO
### VÍRGULA E NÃO É NECESSÁRIO PARENTESIS


#umaTupla = 85,
#print(umaTupla)
pi = 3.14,
print(type(pi))
conta = 2 * pi[0]
print(2 * pi)
print(conta)

tupla = (11, 12, 13, 14, 15, 11)
print(tupla[0])
print(tupla[-1])
print(type(tupla))
print(tupla[0:3])
print(11 in tupla)
lista = list(tupla)
print(type(lista))
#saída entre [] = lista
#saída entre () = tupla
print(lista)

#recuperar o índice de determinado elemento da tupla
print(tupla.index(11))

#quantas vezes o elemento aparece na tupla
print(tupla.count(11))

