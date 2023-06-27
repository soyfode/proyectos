import numpy as np
import scipy as sc
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from math import pi
from pandas.plotting import scatter_matrix
from pandas.plotting import andrews_curves
from sklearn.preprocessing import StandardScaler

#data
df = pd.read_csv("data/data.csv")

#############################################
############# DATA ANALYSIS #################
#############################################
# contar valores para cada grupo de variables 
df["diagnosis"].value_counts()
sns.countplot(x=df['diagnosis'])
plt.show()
#Tipos de datos
df.info()
#Valores núlos
print("Hay valores nulos?",df.isnull().values.any())
# Donde estan
df['Unnamed: 32'].head()
# Borrar Unnamed: 32 y la columna ID
df.drop("id",axis=1,inplace=True)
df.drop("Unnamed: 32",axis=1,inplace=True)
#Valores núlos
print("Hay valores nulos?",df.isnull().values.any())

##### BOXPLOT
plt.figure(figsize=(20,8))
sns.boxenplot(df)
plt.xticks(rotation=90)
plt.show()
# estadarizar
y=df[df.columns[0]]
df_features = df[df.columns[1:]]
scalar = StandardScaler()
scaled_features = scalar.fit_transform(df_features.values)
df_features_scaled = pd.DataFrame(scaled_features,index=df_features.index,columns=df_features.columns)
plt.figure(figsize=(14,8))
sns.boxenplot(df_features_scaled)
plt.xticks(rotation=90)
plt.show()
# Eliminando atípicos
df_features_clean=df_features_scaled[df_features_scaled.apply(lambda x: np.abs(x - x.mean()) / x.std() < 6).all(axis=1)]
print(df_features_clean.shape)
plt.figure(figsize=(14,8))
sns.boxplot( data = df_features_clean )
plt.xticks(rotation=90)  
plt.show()
#Boxplots para cada variable divididos por grupos en Especie
df_features_y_clean = pd.concat([df_features_clean, y], axis=1, join_axes=[df_features_clean.index])
df_features_clean = df_features_y_clean.iloc[:,0:30]
df_y = df_features_y_clean.iloc[:,30]
plt.figure(figsize=(14,8))
df_features_y_clean.boxplot(by="diagnosis", figsize=(24, 12))
plt.xticks(rotation=90)
