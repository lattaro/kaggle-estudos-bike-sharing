import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

BaseDados = pd.read_csv('D:\\Python\\Kaggle\\Bike Sharing Demand\\train.csv')
#print(BaseDados.describe()) #Traz informações como desvio padrão, média, valor mínimo e máximo de colunas, etc.
#print(BaseDados.sample(5).T) #Traz uma amostra da base de dados.
#print(BaseDados)

#print (BaseDados.atemp.describe()) #Faz um describe na coluna atemp 
#print (BaseDados.atemp.value_counts()) #Aplica um value_counts (agrupa informações e faz a soma por linhas do dataset.)
#print (BaseDados.atemp.mode()) #Aplica Moda na coluna atemp
#print(BaseDados[['temp','atemp']].describe()) #Faz um descibre nas colunas temp e atemp
#print (BaseDados.loc[20:30,'workingday':'humidity']) #imprime as linhas 20-30 e as colunas específicas com .loc
#print(BaseDados.iloc[20:31,3:8]) #Faz o mesmo que a linha acima mas usando o método iloc.
#print(BaseDados.at[20,'humidity']) #Traz o valor da célula da linha 20 e da coluna humidity
#print(BaseDados.iat[20,7]) #Faz o msm q a anterior mas com o método iat, que funciona por index
BaseDados['datetime'] = pd.to_datetime(BaseDados['datetime']) #Transforma a coluna datetime no tipo datetime64[ns]
BaseDados['year'] = BaseDados['datetime'].dt.year #cria uma nova coluna chama year por meio do método dt.
BaseDados['day'] = BaseDados['datetime'].dt.day #cria uma nova coluna chama day por meio do método dt.
BaseDados['dayofweek'] = BaseDados['datetime'].dt.dayofweek #cria uma nova coluna chama dayofweek por meio do método dt.
BaseDados['hour'] = BaseDados['datetime'].dt.hour #cria uma nova coluna chama hour por meio do método dt.
#print(BaseDados.temp.median()) #Calcula a mediana da coluna temp.
#print(BaseDados[BaseDados['temp'] > BaseDados['temp'].median()]) #mostra o dados que possuem temp maior que a mediana de temp.
#print(BaseDados.season.value_counts()) #mostra quantas entradas existem para cada seaso. Ex: 2734 season 4.
#BaseDados['temp'].hist() #histograma da coluna temp
#plt.show() #imprime o gráfico
