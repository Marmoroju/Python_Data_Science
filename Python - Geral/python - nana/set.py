# Set não tem retorno de dados duplicados.
# o retorno não é na ordem da listagem
my_set = {"janeiro", "fevereiro", "março", "março"}
for el in my_set:
    print(el)

my_set.add("abril")
print(my_set)