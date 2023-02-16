import sys
sys.path.append("..")
from diabetes import *

################## Creando matrices características y objetivos #########################
#########################################################################################
X = diabetes_df.drop('glucose', axis=1).values
y = diabetes_df['glucose'].values
#########################################################################################
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

####### Segundo tipo de regresión regularizada: Lasso Regression (Lasso) ################
"""
Lasso Regression (Lasso) es una variante de la regresión lineal donde el costo de minimizar 
la suma de los errores al cuadrado se modifica para minimizar la suma de los errores al 
cuadrado+alfa*suma de los valores absolutos de los coeficientes.
"""

scores = []

for alpha in [0.1, 1.0, 10.0, 100.0, 1000.0]:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_train, y_train)
    y_pred = lasso.predict(X_test)
# Guardamos el valor R-cuadrado de modelo en la lista de puntación
scores.append(lasso.score(X_test, y_test)) 

"""
La regresión lazo se puede utilizar para evaluar la importancia de las características. 
El cual reduce a cero los coeficientes de las características menos importantes
"""

names = diabetes_df.drop("glucose", axis=1).columns
lasso = Lasso(alpha=0.1)
lasso_coef = lasso.fit(X, y).coef_
plt.bar(names, lasso_coef)
plt.xticks(rotation=45)
plt.show()
