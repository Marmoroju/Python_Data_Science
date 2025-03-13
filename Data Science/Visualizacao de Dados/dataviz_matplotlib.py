import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Verifica os datasets disponíveis. Exige conexão com a internet
dataset = sns.get_dataset_names()
#print(dataset)

# Carrega um dataset (Método 01)
#df = sns.load_dataset('tips')
#print(df)

# Coleta de dados (Método 02)
df = pd.read_csv('tips.csv')
#print(df)

# Renomear as colunas
df.columns = ["Total da Conta", "Valor da Gorjeta", "Sexo", "Fumante", "Dia", "Horário", "Quantidade de Pessoas"]
#print(df)

# Agrupa os dados por DIA
df1 = df.groupby(["Dia"])

# Calcula a soma das variáveis de acordo com a variável "Dia" e reinicia o índice
dfSoma = df1.sum(["Total da Conta", "Valor da Gorjeta", "Quantidade de Pessoas"]).reset_index()
#print(dfSoma) 

# GRÁFICO DE BARRAS == "ax.bar"
'''fig, ax = plt.subplots(figsize=(10,6)) #cria uma figura com eixos simples(x, y)
ax.bar(dfSoma["Dia"], dfSoma["Valor da Gorjeta"]) #cria o gráfico definido pelos valores do eixo x e y respectivamente
ax.set_title("Soma das gorjetas em relação ao dia da semana", fontsize = 16)
ax.set_xlabel("Dia da Semana", fontsize = 12)
ax.set_ylabel("Soma das gorjetas (US$)", fontsize = 12)
for p in ax.patches: #exibe os valores no gráfico
    _x = p.get_x() + p.get_width() - 0.5
    _y = p.get_y() + p.get_height()
    value = int(p.get_height()) # onde os valores serão apresentados
    ax.text(_x, _y, value, ha="left")
plt.show()'''

# GRÁFICO DE BARRAS HORIZONTAL == "ax.barh"   
'''fig, ax = plt.subplots(figsize=(10,6)) #cria uma figura com eixos simples(x, y)
ax.barh(dfSoma["Dia"], dfSoma["Valor da Gorjeta"]) #cria o gráfico definido pelos valores do eixo x e y respectivamente
ax.set_title("Soma das gorjetas em relação ao dia da semana", fontsize = 16)
ax.set_xlabel("Soma das gorjetas (US$)", fontsize = 12)
ax.set_ylabel("Dia da Semana", fontsize = 12)
for p in ax.patches: #exibe os valores no gráfico
    _x = p.get_x() + p.get_width() 
    _y = p.get_y() + p.get_height() - 0.5
    value = int(p.get_width()) # onde os valores serão apresentados
    ax.text(_x, _y, value, ha="left")
plt.show()'''

# GRÁFICO DE BARRAS VERTICAIS AGRUPADAS
'''diasDaSemana = dfSoma["Dia"] #salva a lista de dias da semana
ax = dfSoma.plot.bar(rot=0, figsize=(10,6))
ax.set_title("Visão Geral", fontsize=16)
ax.set_xlabel("Dia da Semana", fontsize=12)
ax.set_ylabel("Valor", fontsize=12)
ax.set_xticklabels(diasDaSemana) #exibe os nomes dos dias da semana
ax.get_legend()
for p in ax.patches:
    _x = p.get_x() + p.get_width() - 0.17
    _y = p.get_y() + p.get_height()
    value = int(p.get_height())
    ax.text(_x, _y, value, ha="left")
plt.show()'''

# GRÁFICO DE DISPERSÃO == 'ax.scatter'
# Os dados da variável INDEPENDENTE ficam no eixo x e s dados da variável DEPENDENTE ficam no eixo y do gráfico
# https://matplotlib.org/stable/api/markers_api.html

# define as cores dos marcadores
'''np.random.seed(196)
qtdCores = 4
cores = np.random.rand(qtdCores)

fig, ax = plt.subplots()
ax.scatter(dfSoma["Quantidade de Pessoas"], dfSoma["Valor da Gorjeta"], c = cores, marker = "8") #define os valores para o eixo x e para o eixo y respectivamente
ax.set_title("Soma das gorjetas em relação ao total das pessoas", fontsize=16)
ax.set_xlabel("Total de pessoas", fontsize=12)
ax.set_ylabel("Soma das gorjetas (US$)", fontsize=12)
plt.grid()
plt.show()'''

# GRÁFICO DE LINHAS == 'ax.plot'
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
'''fig, ax = plt.subplots() # cria uma figura com eixos simples (x, y)
ax.plot(dfSoma.Dia, dfSoma["Valor da Gorjeta"], marker = "8", label = "Valor da Gorjeta") # Define a primeira linha
ax.plot(dfSoma.Dia, dfSoma["Total da Conta"], marker = "8", label = "Total da Conta") # Define a segunda linha
ax.plot(dfSoma.Dia, dfSoma["Quantidade de Pessoas"], marker = "8", label = "Quantidade de Pessoas") # Define a terceira linha
ax.set_title("Comportamento da variáveis em relação ao dias da semana", fontsize = 16)
ax.set_xlabel("Dias da semana", fontsize = 12)
ax.legend(loc = "best", bbox_to_anchor=(0.5, 0.5))
plt.grid()
plt.show()
'''

# BOXPLOT 
# Permite visualizar a distribuição de dados de uma variável divididos entre quartis
# Quartis são valores que dividem um conjunto de elementos ordenados em quatro parte iguais, ou seja, cada parte contém 25% desses elementos
# Exibe onde a maioria dis dados sen encontra e se há outliers
# Exime uma análise visual da posição, dispersão, simetria, caudas e outliers do conjunto de dados:
# - Posição: Observa-se a linha central do retângulo que é a mediana ou segundo quartil;
# - Outliers: valores atípicos, ou seja, que se afastam da maioria dos valores encontrados no conjunto de dados;
# - Dispersão: representada pela caixa, indica onde a maioria dos dados se encontra;
# - Cauda: os valores no fim da cauda tem uma probabilidade de ocorrência muito baixa;
# - Simetria: a distribuição dos dados é simétrica quanto as três medidas de tendência central, média, mediana e moda são iguais.
'''
variavelAnalisada = ["Valor da Gorjeta"]
fig, ax = plt.subplots()
ax.boxplot(df["Valor da Gorjeta"], labels = variavelAnalisada)
ax.set_title("Análise do valor das gorjetas", fontsize=16)
plt.grid()
plt.show()
'''

# MULTIPLAS BOXPLOTS
'''variaveisAnalisadas = ["Valor da Gorjeta", "Quantidade de Pessoas"]
dados = [df["Valor da Gorjeta"], df["Quantidade de Pessoas"]]
fig, ax = plt.subplots()
ax.boxplot(dados, labels=variaveisAnalisadas)
ax.set_title("Multiplos Boxplots", fontsize=16)
plt.grid()
plt.show()'''

# HISTOGRAMA
# Gráfico de barras que exibe a distribuição de frequências dos dados;
# A base de cada uma das barras representa uma classe de dados e a altura representa a quantidade ou frequencia absoluta com que o valor de cada classe ocorre;
# Exibe a dispersão dos dados, ou seja, onde a maioria dos dados se encontra.
'''
fig, ax = plt.subplots()
ax.hist(df["Valor da Gorjeta"], bins=10)
ax.set_title("Histograma do Valor da Gorjeta", fontsize=16)
ax.set_xlabel("Valor da Gorjeta", fontsize=12)
ax.set_ylabel("Frequência", fontsize=12)
for p in ax.patches:
    _x = p.get_x() + p.get_width() - 0.6
    _y = p.get_y() + p.get_height()
    value = int(p.get_height())
    ax.text(_x, _y, value, ha="left")
plt.show()'
'''

# GRÁFICO DE PIZZA
# Indicado quando se deseja expressar uma relação de proporcionalidade, em que todos os valores somados compôem o todo de uma variável;
# Desenhado em formato circular e dividido em setores, sendo as suas áreas diretamente proporcionais às frequências correspondentes;
# Os setores devem ter cores diferentes e identificados em uma legenda;
# Não é recomendado quando existem muitos setores ou faatias.

#print(dfSoma)

# Cria uma nova coluna com o percentual de pessoas em relação ao dia da semana
dfSoma["Percentual %"] = round((dfSoma["Quantidade de Pessoas"] / dfSoma["Quantidade de Pessoas"].sum())* 100, 2)
#print(dfSoma)
'''
diasDaSemana = dfSoma.Dia #salva  lista de dias da semana
percentuais = dfSoma["Percentual %"] #salva a lista com os percentuais
explode = (0, 0.1, 0, 0) #explode somente a segunda fatia

fig, ax = plt.subplots()
ax.pie(percentuais, explode=explode, labels=diasDaSemana, autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title("Percentual de pessoas por dia", fontsize=16)
ax.axis('equal') #garante que o gráfico seja desenhado no formato de circulo
plt.show()
'''


# FACETS
# Facets são um excelente recurso que permite segmentar um gráfico e dividir a visualização em porcões menores, lado a lado.

# define as cores dos marcadores
'''np.random.seed(18)
qtdCores = 4
cores = np.random.rand(qtdCores)

fig, axs = plt.subplots(1, 3, figsize=(9,3)) #define as caracteristicas do Facet
axs[0].scatter(dfSoma["Dia"], dfSoma["Valor da Gorjeta"], c=cores, marker="8")
axs[0].set_xlabel("Dia")
axs[0].set_ylabel("Soma das Gorjetas")
axs[1].scatter(dfSoma["Quantidade de Pessoas"], dfSoma["Valor da Gorjeta"], c=cores, marker="8")
axs[1].set_xlabel("Quantidade de Pessoas")
axs[2].scatter(dfSoma["Total da Conta"], dfSoma["Valor da Gorjeta"], c=cores, marker="8")
axs[2].set_xlabel("Total da Conta")
fig.suptitle('Facet da soma total das gorjetas')
plt.show()'''



