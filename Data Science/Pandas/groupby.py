import pandas as pd
import numpy as np

# Dividir o dataset em grupos com base em algum critério;
# Aplicar funcões para cada grupo independente;
# Combinar os resultados em uma estrutura de dados.

 

df = pd.read_csv('titanic/train.csv')
#print(df)

# Excluir colunas específicas
df = df.drop(['PassengerId', 'Name'], axis=1)
#print(df)

df.columns = ['Sobrevivente', 'Classe', 'Sexo', 'Idade', 'Quantidade de irmãos e esposas', 'Quantidade de pais e filhos', 'Bilhete', 'Tarifa', 'Cabine', 'Porto de Embarque']
#print(df)

# Analizando os dados setando a variável Sobrevivente como índice
#OBS.: FUNCIONA COMO A WINDOW FUNCTION 'OVER (PARTITION BY)' DO ORACLE SQL
df1 = df.groupby('Sobrevivente')
#print(df1)

# Verifica a quantidade de sobreviventes e não soberviventes
df1.Sobrevivente.size()

# Verifica a MÉDIA das variáveis numéricas de acordo com a variável sobrevivente
media = df1[['Idade', 'Quantidade de irmãos e esposas', 'Quantidade de pais e filhos', 'Tarifa']].aggregate(['mean'])
#print(media)

# Verifica a MEDIANA das variáveis numéricas de acordo com a variável sobrevivente
mediana = df1[['Idade', 'Quantidade de irmãos e esposas', 'Quantidade de pais e filhos', 'Tarifa']].aggregate(['median'])
#print(mediana)

# Verifica o valor MÁXIMO e MÍNIMO das variáveis numéricas de acordo com a variável sobrevivente
minMax = df1[['Idade', 'Quantidade de irmãos e esposas', 'Quantidade de pais e filhos', 'Tarifa']].aggregate(['min', 'max'])
#print(minMax)

# Indexa a variável Sobrevivente e sexo
df2 = df.groupby(['Sobrevivente', 'Sexo'])
quantidade = df2.size().reset_index().rename(columns = {0: 'Quantidade'})
#print(quantidade)







