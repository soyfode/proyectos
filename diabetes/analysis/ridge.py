import sys
sys.path.append("..")
from diabetes import *

################## Creando matrices características y objetivos #########################
#########################################################################################
X = diabetes_df.drop('glucose', axis=1).values
y = diabetes_df['glucose'].values
#########################################################################################
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

############################## REGRESION REGULARIZADA ###################################
# Se usa para evitar el sobre ajuste

#########################################################################################
####### Primer tipo de regresión regularizada: Ridge Regression (cresta) ################
#########################################################################################
"""
Ridge Regression (cresta) es una variante de la regresión lineal donde el costo de 
minimizar la suma de los errores al cuadrado se modifica para minimizar la suma de los 
errores al cuadrado+alfa*suma de los cuadrados de los coeficientes.
"""

scores = []

for alpha in [0.1, 1.0, 10.0, 100.0, 1000.0]:
    rigde = Ridge(alpha=alpha)
    rigde.fit(X_train, y_train)
    y_pred = rigde.predict(X_test)
# Guardamos el valor R-cuadrado de modelo en la lista de puntación
scores.append(rigde.score(X_test, y_test)) 

print(scores)

