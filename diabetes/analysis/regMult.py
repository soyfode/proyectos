import sys
sys.path.append("..")
from diabetes import *

# Creando matrices características y objetivos
##############################################
X = diabetes_df.drop('glucose', axis=1).values
y = diabetes_df['glucose'].values
##############################################


"""
Regresión lineal para predecir los niveles de glucosa en la sangre utilizando todas las 
características del conjunto de datos de diabetes.
"""
# Dividimos los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
reg_all = LinearRegression()
reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test) # predice el conjunto de prueba
# R cuadrado
print(reg_all.score(X_test, y_test))
# Calcular RMSE (Raíz del error cuadrático medio)
print(mean_squared_error(y_test, y_pred, squared=False))
# donde el modelo tiene un error medio para los niveles de glucosa en la sangre de 42.5 mg/dl
