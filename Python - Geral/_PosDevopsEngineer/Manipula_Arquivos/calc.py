arquivo = open('C:/Users/Marcos/pY/cap06/teste.txt', 'r')
conta = arquivo.readline()
arquivo.close()
conta = conta.split()



resultado = ""
if conta[1] == "+":
    resultado = int(conta[0]) + int(conta[2])
elif conta[1] == "-":
    resultado = int(conta[0]) - int(conta[2])
elif conta[1] == "x":
    resultado = int(conta[0]) * int(conta[2])
elif conta[1] == "/":
    resultado = int(conta[0]) / int(conta[2])

resultado = str(resultado)
print(f'A operação: {conta[0]} {conta[1]} {conta[2]} é {resultado}')
arquivo = open('C:/Users/Marcos/pY/cap06/teste.txt', 'a')
arquivo.write(resultado)
arquivo.close