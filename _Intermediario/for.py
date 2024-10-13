#capitais = ["Salvador", "Aracaju", "Maceió"]
#
#for k in capitais:
#    print(k)
#
#tupla = "Ciência", 2.0, 45,
#for i in tupla:
#    print(i)
#
#frase = ("Ciência de Dados")
#for i in frase:
#    print(i)
#else:
#    print(len(frase))    

#dicionario = {"chave1": "big", "chave2": "data", "chave3": 56.8}
#for chave in dicionario.items():
#    print(chave)
#else:
#    print(f'{len(dicionario)} elementos foram listados')    

#contador = 0
##sintaxe range(start, stop, step)
#for i in range(2,10,2):
#    print(i)
#    contador += 1
#else:
#    print(f'{contador} elementos foram listados')    

#contador = 0
#for i in range(2,11):
#    if i % 2 == 0:
#        print(i)
#        contador += 1
#else:
#    print(f'{contador} elementos foram listador')        

#listaDeListas = [[1, 2, 3], #lista 01
#                 [4, 5 ,6], #lista 02
#                 [7, 8, 9]] #lista 03
##loop aninhado
#y = 0
#for i in listaDeListas: # percorre a lista 01, depois a 02 e por último a 03
#    print(listaDeListas[y])
#    y += 1
#    for x in i: # percorre os elementos de cada lista.
#        print(x) # imprime os elementos da lista atual que está sendo percorrida
    
#contador = 0
#for numero in range(10):
#    if numero == 5:
#        break
#    print(numero)
#    contador += 1
#else:
#    print("O loop chegou ao fim")    
#print(f'{contador} elementos foram listados')    

#contador = 0
#for numero in range(10):
#    if numero == 5:
#        continue # break, then continue
#    print(numero)
#    contador += 1
#else:
#    print(f'{contador} elementos foram listados') 

#from random import randint
#
#umaLista = []
#for i in range(6):    
#    num = randint(8,18)
#    umaLista.append(num)
#    forca = umaLista[0:1]
#    dext = umaLista[1:2]  
#    cons = umaLista[2:3]  
#    inte = umaLista[3:4]  
#    sabe = umaLista[4:5]  
#    cari = umaLista[5:6]  
#    atributos = [forca, dext, cons, inte, sabe, cari]
#else:
#    print(f'Os dados rolaram {umaLista}\ne seus atributos foram distribuídos desta forma:')
#    print(f'Força {atributos[0]}\nDestreza {atributos[1]}\nConstituição {atributos[2]}\nInteligência {atributos[3]}\nSabedoria {atributos[4]}\nCarisma {atributos[5]}\n')   


