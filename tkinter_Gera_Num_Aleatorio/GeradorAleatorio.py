from tkinter import *
import random

def gerador():
  numInicial = int(a.get())
  numFinal = int(b.get())
  gerar = int(c.get())
  aleatorio = random.sample(range(numInicial, numFinal), gerar)
  #print(aleatorio)

  texto = f'''
  Números Gerados: {aleatorio}'''

  numAleatorio["text"] = texto


tabela = Tk()
tabela.title("Gerador de Números Aleatórios")
tabela.geometry("400x300")

aA = Label(tabela, text="Digite o número inicial:").grid(column=0, row=0)
a = Entry(tabela)
a.grid(column=1, row=0, pady=10)

bB = Label(tabela, text="Digite o número final:").grid(column=0, row=1)
b = Entry(tabela)
b.grid(column=1, row=1, pady=10)

cC = Label(tabela, text="Quantos números deseja gerar?").grid(column=0, row=2)
c = Entry(tabela)
c.grid(column=1, row=2, pady=10)

btn = Button(tabela, text="Gerar", command=gerador)
btn.grid(column=1, row=3, pady=10)

numAleatorio = Label(tabela, text="")
numAleatorio.grid(column=0, row=4)

tabela.mainloop()