##############################################
#Librerias
library(ggplot2)
library(ggthemes)
library(showtext)
library(magick)
library(readr)
library(dplyr)
library(tidyr)

#DATA
# LIBERTAD ECONÓMICA
freedom <- read_csv("data/freedom-scores.csv", 
                           col_types = cols(`Overall Score` = col_number()))
# Puntaje más alto mas libertad económica
# Puntaje más bajo menos libertad económica

# FRASER
fraser = read.csv("data/fraser.csv",dec = ",")

# IDH
idh = read.csv("data/idh.csv")
idh = select(idh,iso3:hdi_2021)
# IDH alto (0.800 o superior): Indica un nivel de desarrollo humano muy alto. 
#Los países con un IDH alto suelen tener una esperanza de vida más larga, 
#una educación más accesible y de calidad, así como un ingreso per cápita más alto. 
#Estos países suelen ofrecer un buen nivel de bienestar y oportunidades para 
#sus ciudadanos.

#IDH medio (0.500-0.799): Indica un nivel de desarrollo humano medio. 
#Los países con un IDH medio pueden mostrar una mezcla de avances en áreas como 
#la esperanza de vida, la educación y el ingreso, pero aún tienen margen de 
#mejora en algunas dimensiones del desarrollo humano.

#IDH bajo (inferior a 0.500): Indica un nivel de desarrollo humano bajo. 
#Los países con un IDH bajo suelen tener una esperanza de vida más corta, 
#acceso limitado a la educación y bajos ingresos per cápita. Estos países 
#enfrentan desafíos significativos en términos de desarrollo humano y pueden
#requerir medidas y políticas adicionales para mejorar las condiciones de 
#vida de su población.

#GINI
gini = read.csv("data/gini.csv")



#Bolivia 1995-2023
freedomBo = subset(freedom,Name=="Bolivia")
freedomBo = freedomBo %>%
  rename("año"="Index Year")%>%
  rename("ile"="Overall Score")

idhBo = subset(idh,iso3=="BOL")
idhBo = gather(idhBo,key="año",value = "idh",hdi_1995:hdi_2021)
idhBo = idhBo %>%
  mutate_all(~gsub("^hdi_","",.))
idhBo$año = as.numeric(idhBo$año)
idhBo$idh = as.numeric(idhBo$idh)
idhBo$idh = idhBo$idh*100

giniBo = subset(gini,Country.Code=="BOL")
giniBo = gather(giniBo,key="año",value = "gini",X1995:X2022)
giniBo = giniBo %>%
  mutate_all(~gsub("^X","",.))
giniBo$año = as.numeric(giniBo$año)
giniBo$gini = as.numeric(giniBo$gini,na.action="na.pass")

fraserBo = subset(fraser,Countries=="Bolivia")
fraserBo = fraserBo %>%
  rename("fraser"="Economic.Freedom.Summary.Index")%>%
  rename("año"="Year")
fraserBo = subset(fraserBo,año>=1995)
fraserBo$fraser = fraserBo$fraser*10


indexBo <- merge(freedomBo,idhBo, by = "año",all = TRUE)
indexBo <- merge(indexBo,giniBo, by = "año",all = TRUE)
indexBo <- merge(indexBo,fraserBo, by = "año",all = TRUE)


font_add_google("Abril Fatface", "font")
showtext_auto()
 
ggplot(data=indexBo) +
  
  annotate("rect", xmin = -Inf, xmax = 1997, ymin = -Inf, ymax = 72, fill = "#ec84ac", color = NA,alpha=.2) +
  annotate("rect", xmin = 1997, xmax = 2001, ymin = 61, ymax = 72, fill ="#fc040c", color = NA,alpha=.2) +
  annotate("rect", xmin = 1997, xmax = 2001, ymin = 51, ymax = 61, fill ="#ffffffff", color = NA,alpha=.2) +
  annotate("rect", xmin = 1997, xmax = 2001, ymin = -Inf, ymax = 51, fill ="black", color = NA,alpha=.2) +
  annotate("rect", xmin = 2002, xmax = 2005, ymin = -Inf, ymax = 72, fill = "#ec84ac", color = NA,alpha=.2) +
  annotate("rect", xmin = 2006, xmax = 2019, ymin = -Inf, ymax = 72, fill ="#3D5D95", color = NA,alpha=.2) +
  annotate("rect", xmin = 2020, xmax = Inf, ymin = -Inf, ymax = 72, fill ="#3D5D95", color = NA,alpha=.2) +
  
  annotate("text", x = 1995, y = 73, label = "MNR", color = "#3D5D95",size=6,fontface=2,alpha=1,family="font")+
  annotate("text", x = 1999, y = 73, label = "ADN", color = "#3D5D95",size=6,fontface=2,alpha=1,family="font")+
  annotate("text", x = 2003.5, y = 73, label = "MNR", color = "#3D5D95",size=6,fontface=2,alpha=1,family="font")+
  annotate("text", x = 2012.5, y = 73, label = "MAS", color = "#3D5D95",size=6,fontface=2,alpha=1,family="font")+
  annotate("text", x = 2022.2, y = 73, label = "MAS", color = "#3D5D95",size=6,fontface=2,alpha=1,family="font")+
  
  stat_smooth(aes(x = año, y = ile), method = "loess", color = "#b0536f", size = 2.5, se = FALSE, linetype = 1) +
  stat_smooth(aes(x = año, y = idh), method = "loess", color = "#9bbc61", size = 2.5, se = FALSE, linetype = 1) +
  stat_smooth(aes(x = año, y = gini), method = "loess", color = "#71d7d1", size = 2.5, se = FALSE, linetype = 1) +
  stat_smooth(aes(x = año, y = fraser), method = "loess", color = "#ea6472", size = 2.5, se = FALSE, linetype = 1) +
  
  geom_rect(aes(xmin = 1994.8, xmax = 2003.6, ymin = 41, ymax = 49), fill = "#3D5D95", color = "#355671", size = 1) +
  
  geom_label(aes(x = 1999.2, y = 44,
                 label = "Indice de Libertad económica: Heritage"),
             stat = "unique",
             size = 8, color = "#fbf2e3",fill="#b0536f",family="font")+ 
  geom_label(aes(x = 1998.05, y = 48,
                 label = "Indice de Desarrollo Humano"),
             stat = "unique",
             size = 8, color = "#fbf2e3",fill="#9bbc61",family="font")+
  geom_label(aes(x = 1995.95, y = 42,
                 label = "Indice GINI"),
             stat = "unique",
             size = 8, color = "#fbf2e3",fill="#71d7db",family="font")+
  geom_label(aes(x = 1999, y = 46,
                 label = "Indice de Libertad Económica: Fraser"),
             stat = "unique",
             size = 8, color = "#fbf2e3",fill="#ea6472",family="font")+
  
  labs(x = "", y = "", caption = "FUENTE: The Heritage foundation, Fraser Institute, Wold Bank, PNUD. Datos suavizados. @soy_fode", title = "LIBERTAD ECONÓMICA, \nGINI e IDH: BOLIVIA") +
  theme_tufte() +
  theme(
    text = element_text(family = "font", size = 13, color = "#3D5D95"),
    plot.title = element_text(hjust = .95, vjust = -35, color = "#3D5D95", face = "bold", size = 50),
    plot.margin = margin(-80, 30, 10, 10, unit = "pt"),
    axis.title.x = element_text(color = "#3D5D95"),
    axis.title.y = element_text(color = "#3D5D95"),
    axis.text.x = element_text(color = "#3D5D95",size = 17,face="bold"),
    axis.text.y = element_text(color = "#3D5D95",size = 17,face="bold"),
    plot.caption = element_text(size = 10, hjust = 0.5, vjust = -1,color="#fbf2e3"),
    panel.border = element_rect(color = "#3D5D95", fill = NA, size =0),
    plot.background = element_rect(colour = "#3D5D95", fill="#fbf2e3", size=20)
  ) 
  
  



