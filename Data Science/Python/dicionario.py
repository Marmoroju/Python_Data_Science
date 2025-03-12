# {"CHAVE":"VALOR"}
# VALORES PODEM SER MODIFICADOS, AS CHAVES NÃO
#
dicionario = {"chave": "1", "chave2": "34"}
#print(dicionario)
#
##dicionário vazio
#vazio = {}
#
##Inserir ou Deletar
#dicionario["inserido1"] = 80
#print(dicionario)
#
#dicionario["lista"] = ['item1', 'item2']
#print(dicionario)
#
#dicionario["lista"].append("item3")
#print(dicionario)
#
#dicionario["lista"].remove("item3")
#print(dicionario)
#
##dicionario.clear()
#print(dicionario)
#del dicionario

# Atribuir novo valor a chave "Slicing"
di = {"chav" : "valor", "chav2" : "valor2"}
print(di)
di["chav"] = "valor alterado"
print(di)

#atribuir valores as variaveis
a, b = di["chav"], di["chav2"]
print(a)
print(b)

lista = {"lista" : ["item1", "item2"]}
print(lista)
print(lista["lista"][0])

# Métodos dos dicionários "dict"
print(di.keys())
print(di.values())
print(di.items())

conta = lista["lista"].count("item1")
print(conta)

# Adicionar um dicionário ao outro
adicionar = dicionario.update(di)
print(adicionar)


