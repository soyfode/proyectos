# LIBRERIAS
library(wooldridge)
library(lmtest)
library(stats)
library(car)
library(tseries)
library(MASS)

ls(package:wooldridge)
df = corn
pairs(df)

#MCO
rlm=rlm(cornhec~soyhec+cornpix+soypix,data=df)
lm=lm(cornhec~soyhec+cornpix+soypix,data=df)
summary(lm)
summary(rlm)

#Linealidad en los coeficientes(h_0:NO hay evidencia de que los coeficientes de
#los modelo sean no lineales)
resettest(lm) # El modelo es lineal.

#Homocedasticidad de los errores (h_0: No hay evidencia de que la varianza de 
#los errores no sean constante a través de las observaciones.)

#Normalidad de los errores (h_0: Los errores del modelo de regresión siguen una
# distribución normal.)
jarque.bera.test(lm$residuals) # Los errores no sigue una distribución normal

#Independencia de los errores (h_0: No hay evidencia de que los errores estén 
#correlacionados entre sí.)
dwtest(lm)#No estan correlacionados

#Ausencia de multicolinealidad (variables correlacionadas) (Si el VIF de una 
#variable es mayor que 5 o 10, generalmente se considera que hay multicolinealidad en el modelo.)
vif(lm)# No existe multicolinalidad

#Ausencia de correlación entre las variables independientes y el término de 
#error: h_0: no existe correlacion.
bptest(lm)#Es constante

