
#######################################
# MEDIDAS DESCRIPTIVAS MULTIVARIANTES #
#######################################


# LOCALIZACIÓN
# DISPERSIÓN
# DEPENDENCIA


##################################
########## LOCALIZACIÓN ##########
##################################

'" La media de localización clásica para describir datos multivariantes
es el VECTOR DE MEDIAS de dimensión = a la cantidad de variables que
tengamos "'

# Se puede usar la medida de profundidad de Tukey

'" Es una medida utilizada en estadística robusta para evaluar la 
ubicación central de un punto en un conjunto de datos multivariados. "'


##################################
########## DEPENDENCIA ############
##################################

# VARIANZA
# DESVIACIÓN TÍPICA
# COVARIANZA -> Valores altos de la otra = hay dependecia lineal, (+)
# Valores menores de la otra no existe dependencia lineal (signo -)
# COEFICIENTE DE CORRELACIÓN -> si r=0 ausencia lineal.

# MATRIZ DE VARIANZAS Y COVARIANZAS

# Las varianzas son la diagonal
# Cuando |S| = 0 hay algunas variables que son combinaciones lineales de otras
# El rango de la matriz S es el número de variables linealmente independientes
# Si |S|=0 es necesario eliminar las variables redundantes

# MATRIZ DE DATOS CENTRADOS PARA ENCONTRAR LA MATRIZ DE COVARIANZAS

# CORRELACIÓN
# Estandarizar las variables es quitar su media y dividirla por su desviación típica

# MATRIZ DE CORRELACIONES
# Nos permite medir la dependencia 

# Si r=1 hay dependencia positiva y fuerte 
# Si R=-1 hay dependencia negativa y fuerte
# Si r=0 Se interperta como la no existencia de una realación lineal
# entre las dos variables o una dependencia débil.
# r=0 si y sólo si s=0, que diremos que las variables son incorrelacionadas


###############################
# ESTANDARIZACIÓN MULTIVARIANTE
###############################

# y = xS_x^(-1/2)
# La estandarización multivariante elimina la media y también las correlaciones
# entre variables.