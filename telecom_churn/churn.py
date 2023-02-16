# MODELO DE CLASIFICACIÓN

# 1. Construir un clasificador.
# 2. Aprende de los datos que le pasamos.
# 3. Pasamos datos sin etiquetar como entrada.
# 4. Hacemos que prediga etiquetas para esos datos no vistos.  

# A medida que el clasificar aprende de los datos etiquetados, lo llamamos datos de entrenamiento.


# K-NEAREST NEIGHBORS (KNN) (k-vecinos más cercanos)

# La idea es predecir la etiqueta de cualquier punto de datos mirando la k etiquetados más cercanos.
# KNN crea un límite de decisión para predecir si los clientes abandonarán o no el servicio.

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# import csv file
churn_df = pd.read_csv('telecom_churn_clean.csv')

# print(churn_df.head())
# print(churn_df.columns)

X = churn_df[["total_day_charge","total_eve_charge"]].values # Características
y = churn_df["churn"].values # Estado de abandono
#print(X.shape,y.shape)

knn = KNeighborsClassifier(n_neighbors=15) # n_neighbors es el número de vecinos más cercanos que queremos mirar
knn.fit(X,y) # Aprende de los datos de entrenamiento

# ¿Cómo saber si el modelo está haciendo predicciones correctas?, podemos evaluar su desempeño
# La precisión es la fracción de predicciones correctas que el modelo hace sobre los datos de prueba.
# Es común medir los datos en un conjunto de entrenamiento y un conjunto de prueba.

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, # comunmente usamos el 20 o 30 %de nuestros datos como conjunto de prueba
                                                    random_state=42, # Semilla para un generador de números aleatoris que divide los datos.
                                                    stratify=y) # Si la rotación ocurre en el 10 % de las observaciones, queremos que el 10 % de las etiquetas en nuestros conjuntos de entrenamiento y prueba representen la rotación. 

# train_test_split devuelve 4 matrices, 
    # X_train.- datos de entrenamiento
    # X_test.- datos de prueba
    # y_train.- etiquetas de entrenamiento
    # y_test.- etiquetas de prueba

knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train,y_train)
#print(knn.score(X_test,y_test)) # score devuelve la precisión del modelo que es de 0.872

# Interpretación de K
# Modelos simples son underfitting, modelos complejos son overfitting.

# CURVA DE COMPLEJIDAD DEL MODELO
train_accuracies = {}
test_accuracies = {}
neighbors = np.arange(1,26) 
for neighbor in neighbors:
    knn = KNeighborsClassifier(n_neighbors=neighbor)
    knn.fit(X_train,y_train)
    train_accuracies[neighbor] = knn.score(X_train,y_train)
    test_accuracies[neighbor] = knn.score(X_test,y_test)

plt.figure(figsize=(8,6))
plt.title("KNN: Precisión del modelo en función del número de vecinos")
plt.plot(neighbors,train_accuracies.values(),label="Precisión de entrenamiento")
plt.plot(neighbors,test_accuracies.values(),label="Precisión de prueba")
plt.legend()
plt.xlabel("Número de vecinos")
plt.ylabel("Precisión")
#plt.show(block=False)
plt.pause(3)
plt.close()

# K será igual a 13
knn = KNeighborsClassifier(n_neighbors=13)
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
print(knn.score(X_test,y_test)) #R2
print(confusion_matrix(y_test,y_pred)) # Matriz de confusión
# 832 Verdaderos negativos (1ra fila, 1ra columna)
print(classification_report(y_test,y_pred)) # Reporte de clasificación





