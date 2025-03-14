#umaString = "Ciência de Dados"
#print(umaString[0])
#print(len(umaString))
#print(len(umaString.split()))
#print(umaString.split('i'))
#print(umaString[1:])
#print(umaString[:1])
#print('Quantas vezes a letra d aparece: ',umaString.count('d'), 'vezes.')
#print('Em qual posição o caractere D aparece: ',umaString.find('D'))
#print("Dados" in umaString)

##  LISTAS ##
listaDePaises = ["Brasil", "Argentina", "Uruguai", "Paraguai"]
print(listaDePaises[0])

listaDePaises[0] = "Índia"
print(listaDePaises[0])

### INSERIR E DELETAR ITEM DA LISTA ###
listaDePaises.insert(2, "Chile")
print(listaDePaises)

listaDePaises.append("Brasil")
print(listaDePaises)

listaVazia = []
listaVazia.insert(0, 'Brasil')
print(listaVazia)

del listaDePaises[0]
print(listaDePaises)

listaDePaises.remove("Paraguai")
print(listaDePaises)

### .pop o valor excluído é atribuído aquela variável ###
x = listaDePaises.pop(0)
print(f"O item '{x}' foi excluído e armazenado nesta variável")

### LISTAS ANINHADAS ###

print(listaDePaises[0])
