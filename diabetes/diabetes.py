##################################################################################
# DATOS DE SALUD DE LAS MUJERES PARA PREDECIR LOS NIVELES DE GLUCOSA EN LA SANGRE.
##################################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score, KFold
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso

diabetes_df = pd.read_csv('diabetes_clean.csv')
# print(diabetes_df.head())

#####################################################################################################
# - pregnancies -> Número de embarazos
# - glucose -> Niveles de glucosa en la sangre. 
# - diastolic -> Presión diastólica (mm Hg)
# - triceps -> Espesor del pliegue cutáneo del tríceps (mm)
# - insulin -> 2 horas de insulina sérica (mu U / ml)
# - bmi -> Índice de masa corporal (peso en kg / (altura en m) ^ 2)
# - dpf -> Función de pedigrí de diabetes
# - age -> Edad (años)
# - diabetes -> Estado de diabetes (1 = diagnóstico y 0 = ausencia de un diagnóstico)
#####################################################################################################

# Creando matrices características y objetivos
X = diabetes_df.drop('glucose', axis=1).values
# print(X)
y = diabetes_df['glucose'].values

# Predecimos los niveles de glucosa en la sangre a partir de una sola característica: el índice de masa corporal (bmi). Para ello cortamos la columna BMI de X, que es la quinta columna, almacenandola como la variable X_bmi
X_bmi = X[:, 4]
# print(y.shape,X_bmi.shape)

# Ahora debemos formatear como una matriz bidimensional para que scikit-learn lo entienda.
X_bmi = X_bmi.reshape(-1,1)
# print(X_bmi.shape)

# Gráfica de la glucosa y el índice de masa corporal
"""
plt.scatter(X_bmi, y)
plt.ylabel("glucosa en sangre (mg/dl)")
plt.xlabel("Índice de masa corporal")
plt.show()
"""

# Ajuste de un modelo de regresión lineal
"""
reg = LinearRegression() # instanciamos el modelo
reg.fit(X_bmi, y)
predictions = reg.predict(X_bmi)
plt.scatter(X_bmi, y)
plt.plot(X_bmi, predictions)
plt.ylabel("glucosa en sangre (mg/dl)")
plt.xlabel("Índice de masa corporal")
plt.show()
"""

# Regresión lineal para predecir los niveles de glucosa en la sangre utilizando todas las características del conjunto de datos de diabetes.
# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
reg_all = LinearRegression()
reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test) # predice el conjunto de prueba
# R cuadrado
print(reg_all.score(X_test, y_test))
# Calcular RMSE (Raíz del error cuadrático medio)
print(mean_squared_error(y_test, y_pred, squared=False))
# donde el modelo tiene un error medio para los niveles de glucosa en la sangre de 42.5 mg / dl.


# VALIDACIÓN CRUZADA .- Se usa para evaluar la variabilidad de un conjunto de datos y la confiabilidad de cualquier modelo entrenado.

# 1.- Comenzamos dividiendo el conjunto de datos en cinco grupos o pliegues
# 2.- Reservamos el primer pliegue como conjunto de prueba.
# 3.- Entrenamos el modelo en los cuatro pliegues restantes.
# 4.- Calculamos la métrica de interés, como el R cuadrado.
# 5.- Reservamos el segundo pliegue como conjunto de prueba.
# 6.- Entrenamos el modelo en los pliegues restantes.
# 7.- Calculamos la métrica de interés, como el R cuadrado.
# 8. Similar para todos los pliegues.
# 9. Realizamos esto para encontrar los estadísticos de interes, como la media, la mediana y los interalos de confianza al 95 %.
# 10.- Llamaos a este proceso validación cruzada de 5 pliegues o más pliegues.

# OBS: Más pliegues más costo computacional.

# Primero llamamos KFold
kf = KFold(n_splits=6, shuffle=True, random_state=1)
# n_splits -> Cantidad de Pliegues.
# shuffle -> True para mezclar los datos antes de dividirlos en pliegues.
# random_state -> Número para asegurar la reproducibilidad de los resultados.

reg = LinearRegression()
cv_results = cross_val_score(reg, X, y, cv=kf)

# Imprimimos los resultados de la validación cruzada
print(cv_results)

# Imprimimos la media y desviación estandar de los resultados de la validación cruzada
print(np.mean(cv_results), np.std(cv_results))

# calculamos el intervalo de confianza al 95%
print(np.quantile(cv_results, [0.025,0.975]))


# REGRESION REGULARIZADA
# Se usa para evitar el sobre ajuste

# Primer tipo de regresión regularizada: Ridge Regression (cresta)
# Ridge Regression (cresta) es una variante de la regresión lineal donde el costo de minimizar la suma de los errores al cuadrado se modifica para minimizar la suma de los errores al cuadrado + alfa * suma de los cuadrados de los coeficientes.

scores = []

for alpha in [0.1, 1.0, 10.0, 100.0, 1000.0]:
    rigde = Ridge(alpha=alpha)
    rigde.fit(X_train, y_train)
    y_pred = rigde.predict(X_test)
    scores.append(rigde.score(X_test, y_test)) # Guardamos el valor R-cuadrado de modelo en la lista de puntación
# print(scores)

# Segundo tipo de regresión regularizada: Lasso Regression (Lasso)
# Lasso Regression (Lasso) es una variante de la regresión lineal donde el costo de minimizar la suma de los errores al cuadrado se modifica para minimizar la suma de los errores al cuadrado + alfa * suma de los valores absolutos de los coeficientes.

scores = []

for alpha in [0.1, 1.0, 10.0, 100.0, 1000.0]:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    y_pred = lasso.predict(X_test)
    scores.append(lasso.score(X_test, y_test)) # Guardamos el valor R-cuadrado de modelo en la lista de puntación
# print(scores)

# La regresión lazo se puede utilizar para evaluar la importancia de las características. El cual reduce a cero los coeficientes de las características menos importantes

names = diabetes_df.drop("glucose", axis=1).columns
lasso = Lasso(alpha=0.1)
lasso_coef = lasso.fit(X, y).coef_
plt.bar(names, lasso_coef)
plt.xticks(rotation=45)
plt.show()
