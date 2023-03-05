import sys
sys.path.append("..")
from diabetes import *

############################ AJUSTE DE HIPERPARAMETROS ##############################
"""
Ahora exploraremos cómo optimizar nuestro modelo, ajustaremos los parámetros alpha en
ridge/lasso, y n_neighbors en KNN.  Debemos elegir el parámetro correcto.

Contruimos modelos exitosos eligiendo los hiperparámetros correctos:
    1. Podemos probar muchos valores diferentes.
    2. Ajustarlos todos por separado.
    3. Ver que tan bien funcionan.
    4. Elegir los valores valores.

Cuando ajustamos diferentes valores de hiperparámetros, usamos validación cruzada para
evitar el sobreajuste de los hiperparámetror en el conjunto de prueba.

Todavía podemos dividir los datos, pero realizar una validación cruzada en el conjunto 
de entrenamiento.

Retenemos el conjunto de prueba y lo usamos para evaluar el modelo ajustado.
"""

############################## BÚSQUEDA DE CUADRICULA ###############################
"""
Es un ajuste de hiperparámetros.
Realizar una validación cruzada triple para un hiperparámetro puede ser engorroso por
la cantidad de modelos que se deben construir.  En lugar de eso, podemos realizar una 
BUSQUEDA ALEATORIA, que selecciona al azar valores de hiperparámetros en lugar de bus
car exhaustivamente a través de todos las opciones.

Podemos evaluar el desempeño del modelo en el conjunto de prueba pasando a una llamada
del método de puntación de puntos del objeto de búsqueda aleatoria.

A continuación un ejemplo con el dataset de diabetes.
"""

"""
construyamos un modelo de regresión lasso con hiperparámetros óptimos para predecir los 
niveles de glucosa en sangre utilizando las características del conjunto de datos.
"""

X = diabetes_df.drop('diabetes', axis=1).values
y = diabetes_df['diabetes'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
kf = KFold(n_splits=3, shuffle=True, random_state=42)
lasso = Lasso()

# Configurar la cuadrícula de parámetros
param_grid = {'alpha': np.linspace(0.1, 1, 20)}
# Instanciar lasso_cv
lasso_cv = GridSearchCV(lasso, param_grid, cv=kf)

# Ajuste a los datos de entrenamiento
lasso_cv.fit(X_train,y_train)
print("Tuned lasso paramaters: {}".format(lasso_cv.best_params_))
print("Tuned lasso score: {}".format(lasso_cv.best_score_))


"""
Como vimos, GridSearchCV puede ser costoso desde el punto de vista computacional, especial
mente si está buscando en un espacio de hiperparámetros grande. En este caso, puede utili
zar RandomizedSearchCV, que prueba un número fijo de configuraciones de hiperparámetros a 
partir de distribuciones de probabilidad especificadas.
"""

# Crear el espacio de parámetros
params = {"penalty": ["l1", "l2"],
         "tol": np.linspace(0.0001, 1.0, 50),
         "C": np.linspace(0.1, 1.0, 50),
         "class_weight": ["balanced", {0:0.8, 1:0.2}]}

# Instanciar el objeto RandomizedSearchCV
logreg_cv = RandomizedSearchCV(logreg, params, cv=kf)

# Ajustar los datos al modelo
logreg_cv.fit(X_train, y_train)

# Imprimir el parámetro ajustado y la puntuación
print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_))
print("Tuned Logistic Regression Best Accuracy Score: {}".format(logreg_cv.best_score_))
