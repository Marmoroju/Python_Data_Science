import pandas as pd
import numpy as np


dicionario1 = {
    "Coluna1" : pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "Coluna2" : pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "b", "c", "d"]),
    "Coluna3" : pd.Series(np.random.randint(1, 100, size=5), index=["a", "b", "c", "d", "e"]),
}

df1 = pd.DataFrame(dicionario1)
#print(df1)

dicionario2 = {
    "Quantidade" : [12, 3, 4, 16],
    "Valor" : [100, 125, 75, 88]
}

df2 = pd.DataFrame(dicionario2)
#print(df2)

# Dataframe a partir de um arquivo CSV

df3 = pd.read_csv('titanic/train.csv', sep = ',', encoding = 'latin-1')
#print(df3)

# Retorna os valores da coluna
#print(df3["Name"])

# Exibir todas as linhas do Dataframe
#todas_as_linhas = pd.set_option('display.max_rows', df3.shape[0])

# Retorna colunas e linhas específicas
colunas = df3[["Name", "Sex", "Age", "Survived"]][0:3]
#print(colunas)

# Retorna um intervalo de linhas
intervalo = df3.iloc[25:32]
#print(intervalo)

# Retorna linhas específicas
linhasEspecificas = df1.loc[["b","d"]]
#print(linhasEspecificas)

# Pesquisa colunas específicas de determinada condição, neste caso, PassengerId == 30
#id = int(input("digite um ID "))
#nomeEspecifico = df3[["Name", "Sex", "Age", "Survived"]][df3.PassengerId == id]
#print(nomeEspecifico)

# Pesquisando registros em um intervalo da coluna Age
idade = df3[["Name", "Sex", "Age", "Survived"]][(df3.Age >=70) & (df3.Age <= 75)]
#print(idade)

# Pesquisando registros utilizando o método Query
metodoQuery = df3.query("Survived == 1 and Pclass == 1 and Sex == 'female'")
#print(metodoQuery)

# MÉTODOS E ATRIBUTOS DE UM DATAFRAME

# Exibe as 5 primeiras linhas do dataframe
firstLine = df3.head()
#print(firstLine)

# Retorna os índices de um DataFrame
indiceDF = df3.index
#print(indiceDF)

# Retorna o nome das colunas de um Dataframe
nomeColunaDF = df3.columns
#print(nomeColunaDF)

# Retorna os valores das colunas de um Dataframe
# Os valores são automaticamente convertidos para uma matriz Numpy
valores = df3.values
#print(valores)

# Informações sobre o tipo de dados de cada coluna
#info = df3.info()
#print(info)

# Verifica o total de valores únicos por coluna
#unico = df3.nunique()
#print(unico)

# Retorna os valores únicos de uma coluna específica
#unicoValor = df3["Embarked"].unique()
#print(unicoValor)

# Conta o número de linhas
quantidadeDeLinhas = df3.shape[0]
#print(quantidadeDeLinhas)

# Conta o número de linhas
quantidadeDeColunas = df3.shape[1]
#print(quantidadeDeColunas)

# Resumo estatístico das colunas
resumo = df3.describe()
#print(resumo)

# Contagem da frequência de valores de uma variável
contagem = df3.Survived.value_counts()
#print(contagem)

# Renomear todas as colunas
# É OBRIGATÓRIO RENOMEAR TODAS AS COLUNAS
renomearColunas = df3.columns = ['ID', 'Sobreviveu', 'Classe', 'Nome', 'Sexo', 'Idade', 'Quantidade de irmãos e esposas', 'Quantidade de pais e filhos', 'Bilhete', 'Tarifa', 'Cabine', 'Porto de Embarque']
#renomearColunas = df3.head(3)
#print(renomearColunas)

# Renomear colunas específicas. "inplace = True" salva a alteração direto no dataframe
renomearColunas2 = df3.rename(columns = {"ID" : "Código", "Nome" : "Nome Completo"}, inplace = True)
#renomearColunas2 = df3.head(3)
#print(renomearColunas2)

# Imprimindo um dataframe
#print(df2)

# Adicionando uma linha no final do dataframe
df2.loc[len(df2.index)] = [30, 5]
#print(df2)

# Criar uma nova coluna no dataframe com valores nulos
df2["Total"] = np.nan
#print(df2)

# Multiplicando colunas
df2["Total"] = df2.Quantidade * df2.Valor
#print(df2)

# Soma as LINHAS do dataframe e adiciona uma COLUNA com o total
# Ficar atento ao intervalo de linhas e colunas especificando o método iloc

df2["Somatório"] = df2.iloc[:, 0:3].sum(numeric_only=True, axis=1)
#print(df2)

# Soma as COLUNAS do dataframe e adiciona uma LINHA com o total
# Ficar atento ao intervalo de linhas e colunas especificando o método iloc

df2.loc["Total"] = df2.iloc[0:4, :].sum(numeric_only=True, axis=0)
#print(df2)

# Excluir coluna pela índice da mesma
df2 = df2.drop(df2.columns[3], axis=1)
#print(df2)

# Excluir colunas específicas
df2 = df2.drop(['Valor', 'Total'], axis=1)
#print(df2)

# Excluir linhas específicas
df2 = df2.drop([0, 2, 'Total'], axis=0)
df2.reset_index(inplace=True)
#df2 = df2.drop(['index'], axis=1)
#print(df2)

# Excluir linhas baseada em uma condição
df2 = df2.drop(df2[df2.Quantidade < 10].index, axis=0)
df2.reset_index(inplace=True)
df2 = df2.drop(['level_0','index'], axis=1)
#print(df2)

# Definir rótulos para os índices
df2.index = ['a', 'b']
#print(df2)

# criação de um dicionário de listas
dicionario3 = {
    "Unidade" : ['pacote', 'und', 'cx', 'peça'],
    "Valor" :   [100, 125, 75, 88]
}
df4 = pd.DataFrame(dicionario3)
#print(df4)

# Concatenando Dataframes
dfConcatenados = pd.concat([df2, df4], axis='columns')
#print(dfConcatenados)

# VERIFICA SE EXISTEM DADOS DUPLICADOS
# Ocorrem dados duplicados quando uma linha inteira é igual a outra
dadosDuplicados = dfConcatenados.duplicated().sum()
#print(dadosDuplicados)

# Excluindo as linhas com dados duplicados mantendo a primeira ocorrência da linha
# ignore_index=True faz com que índice seja reiniciado
excluirDadosDuplicados = dfConcatenados.drop_duplicates(ignore_index=True, inplace=True)

# Alterar o valor específico no dataframe
df2['Quantidade'] = df2['Quantidade'].replace([16, 30], [5, 8])
#print(df2)

# Alterar valores de uma coluna baseada em uma condição
df2.loc[(df2['Quantidade'] > 1) & (df2['Quantidade'] < 7), 'Quantidade'] = 99
#print(df2) 

# SALVAR O DATAFRAME EM UM ARQUIVO EXCEL. 
# Obs. A pasta onde o arquivo for salvo deve existir.

import os

# gerando um arquivo Excel a partir de um Dataframe

#try:
#    df2.to_excel('teste-df2.xlsx', sheet_name='Planilha1')
#    print('Arquivo Salvo!')
#
#except OSError as mensagemOSError: # Erro de entrada e saída
#    print(mensagemOSError)

# Cria um dataframe a partir de um arquivo excel
#df5 = pd.read_excel('teste-df2.xlsx', sheet_name='Planilha1')
#print(df5)

# Gerando um arquivo CSV a partir de um dataframe
#df2.to_csv('teste-df2.csv')
#df6 = pd.read_csv('teste-df2.csv')
#print(df6)

# COLETANDO AMOSTRAS DE UM DATAFRAME
amostra = df3.sample(n=3)
#print(amostra)

# Retorna uma fração específica do número total de linhas
fracao = df3.sample(frac=0.5)
print(fracao)




