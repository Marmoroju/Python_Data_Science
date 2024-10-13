def minhaFuncao():
    print("Meu objetico é ser um Cientista de Dados")

minhaFuncao()

def soma(a, b):
       return a + b

t = int(input('Escolha um número: '))
y = int(input('Escolha outro número: '))
print(soma(t, y))

#valores podem ser informados direto no parâmetro
print(soma(5,2))

#funcao com número indefinido de parâmetro
def umaFuncao(primeiroParametro, *variosParametros):
      #imprime o valor do primeiro parametro
      print(f"Primero Parametro {primeiroParametro}")

      #imprime o valor dos outros parâmetros
      contador = 0
      for k in variosParametros:
            print(f"O argumento número {contador + 2} passado foi {k}")
            contador += 1

umaFuncao("Cientista", "Python", "Pandas", "Previsao", "TI")

