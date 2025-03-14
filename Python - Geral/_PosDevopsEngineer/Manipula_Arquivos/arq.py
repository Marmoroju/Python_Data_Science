arquiv = open('C:/Users/Marcos/pY/cap06/teste.txt', 'r')

frase = arquiv.readlines()
print(frase)
print(frase[0])
print(frase[1])

arquiv.close()