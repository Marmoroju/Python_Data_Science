# CONCATENANDO LISTAS #
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(lista1)
print(lista2)
print(lista1 + lista2)

a = [10, 20, 30]; b = [40, 50, 60]
a.extend(b)
print(a)

print(10 in a)
print(len(a))
print(max(a))
print(min(a))

lista = ["Itaperuna", "Natividade", "Porciúncula", "Tombos"]
reverso = lista.reverse()
print(reverso)
print(lista.sort())

copia = lista.copy()
print(copia)
print(lista.count("Itaperuna"))
