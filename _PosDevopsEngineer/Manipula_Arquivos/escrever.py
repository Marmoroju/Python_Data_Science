def cadastrar_frase ():
    arquivo = open ('C:/Users/Marcos/pY/cap06/teste.txt', 'a')
    frase = (input("Diga alguma coisa: "))
    frase  += '\n'
    arquivo.write(frase)
    arquivo.close()
cadastrar_frase()    

def visualizar_frase():
    arquivo = open ('C:/Users/Marcos/pY/cap06/teste.txt', 'r')
    for linha in arquivo.readlines():
        print(linha)
    arquivo.close()
visualizar_frase()   



    