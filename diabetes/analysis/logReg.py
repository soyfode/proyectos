import sys
sys.path.append("..")
from diabetes import *

############################## REGRESIÓN LOGÍSTICA ######################################
"""
Se utiliza para la clasificación, este modelo calcula la probabilidad, p, de que una 
observación pertenezca a una clase binaria. 
Por ejemplo, si p > 0.5, la observación se clasifica como 1, de lo  contrario si p< 0.5, se 
clasifica como 0. Tenga en cuenta que la regresión logística produce un límite de decisión
lineal.
"""
"""
construiremos un modelo de regresión logística utilizando todas las características del conjunto 
de datos diabetes_df. El modelo se utilizará para predecir la probabilidad de que los individuos 
del conjunto de prueba tengan un diagnóstico de diabetes.
"""

# Creando matrices características y objetivos
##############################################
X = diabetes_df.drop('diabetes', axis=1).values
y = diabetes_df['diabetes'].values
##############################################

# Instanciamos el clasificador
logreg = LogisticRegression()
# Dividimos nuestros datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Ajustamos el modelo a los datos de entrenamiento
logreg.fit(X_train, y_train)
# Predecimos nuestro conjunto de prueba
y_pred = logreg.predict(X_test)

############################# Predecir probabilidades ###################################
"""
Predecimos las probabilidades de que cada instancia pertenezca a una clase por llamando al
método predict_proba() y pasando las funciones de prueba.
"""
# Devuelve una matriz bidimensional con probabilidades para ambas clases. 
# El individuo no abandonó, o abandonó, respectivamente.
y_pred_probs = logreg.predict_proba(X_test)[:,1]
# El modelo predice una probabilidad 
print(y_pred_probs[:10])


################################### La curva ROC ########################################
"""
Visualiza cómo diferentes umbrales efectan las tasas de verdaderos positivos y falsos 
positivos. Si el umbral es cero, el modelo predice uno para todas las observaciones, lo que
significa que predecirá correctamente todos los valores positivos y predecirá incorrectamente
todos los valores negativos. Si el umbral es uno, el modelo predice cero para todos los datos
lo que significa que tanto las tasas positivas verdaderas como las falsas son cero.
"""
fpr, tpr, thresholds = roc_curve(y_test, y_pred_probs)
"""
fpr: Tasa de falsos positivos
tpr: Tasa de verdaderos positivos
thresholds: Umbral
"""
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Logistic Regression ROC Curve')
plt.show()
"""
El modelo es mucho mejor que adivinar al azar la clase de cada observación.
"""
"""
Si tenemos un modelo con uno para la tasa de verdaderos positivos y cero para la tasa de falsos
positivos, este seria el modelo perfecto. Pero calculamos el área bajo la curva ROC, una métrica
conocida como AUC. Que van de cero a uno, siendo uno el ideal.
"""
print(roc_auc_score(y_test, y_pred_probs))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
