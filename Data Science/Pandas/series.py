import pandas as pd
import numpy as np


np.random.seed(13)
s1 = pd.Series(np.random.randint(1, 100, size=5), index=["a", "b", "c", "d", "e"])
#print(s1)

np.random.seed(11)
s2 = pd.Series(np.random.randint(1, 100, size=5))
#print(s2)
#print(s2[:3])
#print(s2[[4 , 2 , 0]])

dicionario = {"b" : 1,
              "a" : 3,
              "c" : 2}

s3 = pd.Series(dicionario)
#print(s3)

s4 = pd.Series(dicionario, index=["b", "a", "c", "k"])
#print(s4)
#print(s4["c"])
#print('iloc localiza pelo indice')
#print(s4.iloc[1:3])
#print('loc localiza pelo rótulo')
#print(s4.loc[["a", "c"]])

s5 = pd.Series(["Daniel", "Jorge", "Rose", "Ana"])
#print(s5)




# Pesquisando elementos da serie
#print(s1)
#var_a = "a" in s1
#print(var_a)

#maior que
#var_b = s1[s1 > 50]
#print(var_b)

# imprime series
#var_c = s4.values
#print(var_c)

#atribui nome para serie
#print(s4.name)
#var_d = s4.name = "Minha Serie"
#print(var_d)

#calculo da media
#print(s4.mean())

#concatenando series
#novaSerie = pd.concat([s4, s2])
#print(novaSerie)
#novaSerie = pd.concat([s4, s2], ignore_index=True)
#print(novaSerie)

#mostra os percentis 
#print(s4.describe())

#verifica se existe valores nulos
#print(pd.isna(s4))

#operações com series
print(s1 + s1)


