##################################################################################
# DATOS DE SALUD DE LAS MUJERES PARA PREDECIR LOS NIVELES DE GLUCOSA EN LA SANGRE.
##################################################################################

################3### Librerias ###########################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Ridge, Lasso, LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.metrics import mean_squared_error, classification_report, confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
##########################################################

################## DATA #######################
diabetes_df = pd.read_csv('/home/fode/git/proyectos/diabetes/diabetes_clean.csv')
###############################################

#####################################################################################
# - pregnancies -> Número de embarazos
# - glucose -> Niveles de glucosa en la sangre. 
# - diastolic -> Presión diastólica (mm Hg)
# - triceps -> Espesor del pliegue cutáneo del tríceps (mm)
# - insulin -> 2 horas de insulina sérica (mu U / ml)
# - bmi -> Índice de masa corporal (peso en kg / (altura en m) ^ 2)
# - dpf -> Función de pedigrí de diabetes
# - age -> Edad (años)
# - diabetes -> Estado de diabetes (1 = diagnóstico y 0 = ausencia de un diagnóstico)
#####################################################################################





