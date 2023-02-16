import sys
sys.path.append("..")
from diabetes import *

#############################################
######### MATRIZ DE CONFUSIÓN ###############
#############################################

# El objetivo es predecir si cada individuo tiene o no probabilidades de padecer diabetes en función de las características índice de masa corporal (IMC) y edad (en años). Por tanto, se trata de un problema de clasificación binaria. Un valor objetivo de 0 indica que el individuo no tiene diabetes, mientras que un valor de 1 indica que el individuo tiene diabetes.

# Creando matrices características y objetivos
X = diabetes_df.drop(['glucose','pregnancies','diastolic','triceps','insulin','dpf','diabetes'], axis=1).values
y = diabetes_df['diabetes'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
knn=KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Precision -> Porcentaje de predicciones positivas correctas.
# Recall -> Porcentaje de verdaderos positivos identificados correctamente.
# F1 Score -> Media armónica de precisión y recuperación. (precision*Recall)/(Precision+Recall)
# Support -> Número de muestras de la clase verdadera en el conjunto de datos de prueba.

