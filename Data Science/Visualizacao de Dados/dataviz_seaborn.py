import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dataviz_matplotlib import dfSoma, df

# Define o tamanho do gráfico
sns.set_theme(rc = {'figure.figsize':(10,6)})

# define o tema utilizado
'''sns.set_theme(style='darkgrid')

ax = sns.barplot(x=dfSoma["Dia"], y=dfSoma["Valor da Gorjeta"], palette="rocket")
ax.set_title("Soma das gorjetas em relação ao dia da semana")
for p in ax.patches:
    _x = p.get_x() + p.get_width() - 0.4
    _y = p.get_y() + p.get_height()
    value = int(p.get_height())
    ax.text(_x, _y, value, ha="left")
plt.show()'''

# GRÁFICO DE BARRAS VERTICAIS AGRUPADAS
'''sns.set_theme(style="whitegrid")

ax = sns.barplot(x=df["Dia"], y=df["Total da Conta"], hue=df["Sexo"], palette="winter_r", errorbar=None)
ax.set_title("Relação entre o total da conta e o sexo do cliente", fontsize=16)
ax.legend(loc="best", bbox_to_anchor=(0.5, 0, 0.5, 0.5)) # (x, y, width, height)
for p in ax.patches:
    _x = p.get_x() + p.get_width() - 0.25
    _y = p.get_y() + p.get_height()
    value = int(p.get_height())
    ax.text(_x, _y, value, ha="left")
plt.show()'''

# COUNTPLOT
# Cria um gráfico com a frequência absoluta dos valores de uma variável
'''sns.set_theme(style="ticks")
ax = sns.countplot(x=df["Sexo"], palette="Greens_d", order=df["Sexo"].value_counts().index)
ax.set_title("Frequênia absoluta da variável sexo", fontsize=16)
for p in ax.patches:
    _x = p.get_x() + p.get_width() - 0.43
    _y = p.get_y() + p.get_height()
    values = int(p.get_height())
    ax.text(_x, _y, values, ha="left")
plt.show()'''

# GRÁFICO DE DISPERÇÃO
'''sns.set_theme(style="whitegrid")
ax = sns.scatterplot(x=dfSoma["Quantidade de Pessoas"], y=dfSoma["Valor da Gorjeta"])
ax.set_title("Soma das gorjetas em relação ao total de pessoas", fontsize=16)
ax.set_xlabel("Total de pessoas", fontsize=12)
ax.set_ylabel("Soma das gorjetas", fontsize=12)
plt.show()'''


#GRÁFICO DE LINHAS
'''df2 = dfSoma.set_index("Dia")

sns.set_theme(style="darkgrid")
ax = sns.lineplot(data=df2, markers="8")
ax.set_title("Comportamento das variáveis em relação aos dias da semana", fontsize=16)
ax.legend(loc="best")
plt.show()'''

# BOX PLOT
'''ax = sns.boxplot(data=df["Quantidade de Pessoas"], palette="Set2")
ax.set_xticklabels(["Quantidade de Pessoas"])
plt.show()'''

# BOX PLOT MÍLTIPLO
'''ax = sns.boxplot(data=df[["Quantidade de Pessoas", "Valor da Gorjeta"]], palette="Set2")
ax.set_xticklabels(["Quantidade de Pessoas", "Valor da Gorjeta"])
plt.show()'''

# HISTOGRAMA
'''ax = sns.histplot(x=df["Quantidade de Pessoas"], bins=6)
ax.set_title("Histograma de pessoas por mesa", fontsize=16)
ax.set_ylabel("Frequência", fontsize=12)
for p in ax.patches:
    _x = p.get_x() + p.get_width() - 0.5
    _y = p.get_y() + p.get_height()
    values = int(p.get_height())
    ax.text(_x, _y, values, ha="left")
plt.show()'''

# FACET
sns.set_theme(style="darkgrid")
ax = sns.FacetGrid(df, col="Dia", height=5, aspect=0.8)
ax.map(sns.histplot, "Valor da Gorjeta")
plt.show()

# FACET com gráficos de linhas de todas asvariáveis
'''
ax = sns.PairGrid(df)
ax.map(sns.lineplot)
plt.show()
'''






