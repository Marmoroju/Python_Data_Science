#y = 3
#s = -1
#for w in range(y):
#    s += 1
#print(s)

arquivo = open ("C:/Users/Marcos/Documentos/Marcos/exto.txt", 'r')
x = arquivo.readline()
arquivo.close()
x = x.split(";")
print(float(x[0])**float(x[1]))

