import sys
sys.path.append("..")
from diabetes import *

# Creando matrices características y objetivos
##########################################################################################
X = diabetes_df.drop('glucose', axis=1).values
y = diabetes_df['glucose'].values
##########################################################################################

"""
Predecimos los niveles de glucosa en la sangre a partir de una sola característica: el 
índice de masa corporal (bmi). Para ello cortamos la columna BMI de X, que es la quinta 
columna, almacenándola como la variable X_bmi
"""
X_bmi = X[:, 4]
# print(y.shape,X_bmi.shape)

# Ahora debemos formatear como una matriz bidimensional para que scikit-learn lo entienda.
X_bmi = X_bmi.reshape(-1,1)
# print(X_bmi.shape)

# Ajuste de un modelo de regresión lineal
reg = LinearRegression() # instanciamos el modelo
reg.fit(X_bmi, y)
predictions = reg.predict(X_bmi)
plt.scatter(X_bmi, y)
plt.plot(X_bmi, predictions)
plt.ylabel("glucosa en sangre (mg/dl)")
plt.xlabel("Índice de masa corporal")
plt.show()
