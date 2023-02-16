import sys
sys.path.append("..")
from diabetes import *

############################### VALIDACIÓN CRUZADA ##########################################
# Se usa para evaluar la variabilidad de un conjunto de datos y la confiabilidad de cualquier 
# modelo entrenado.

# Creando matrices características y objetivos
##############################################
X = diabetes_df.drop('glucose', axis=1).values
y = diabetes_df['glucose'].values
##############################################

# 1.- Comenzamos dividiendo el conjunto de datos en cinco grupos o pliegues
# 2.- Reservamos el primer pliegue como conjunto de prueba.
# 3.- Entrenamos el modelo en los cuatro pliegues restantes.
# 4.- Calculamos la métrica de interés, como el R cuadrado.
# 5.- Reservamos el segundo pliegue como conjunto de prueba.
# 6.- Entrenamos el modelo en los pliegues restantes.
# 7.- Calculamos la métrica de interés, como el R cuadrado.
# 8. Similar para todos los pliegues.
# 9. Realizamos esto para encontrar los estadísticos de interes, como la media, 
    # la mediana y los interalos de confianza al 95 %.
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

# Imprimimos la media y desviación estándar de los resultados de la validación cruzada
print(np.mean(cv_results), np.std(cv_results))

# calculamos el intervalo de confianza al 95%
print(np.quantile(cv_results, [0.025,0.975]))
