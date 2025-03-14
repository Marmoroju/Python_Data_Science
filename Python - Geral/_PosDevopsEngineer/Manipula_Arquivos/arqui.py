arquivo = open('C:/Users/Marcos/pY/cap06/teste.txt', 'r')

for texto in arquivo.readlines():
    print(texto)

arquivo.close