
#Library
library(tidyverse)
library(ggplot2)
library(ggthemes)
library(showtext)
library(emojifont)
library(fontawesome)

#data
df = read.csv("data/secuestroDroga.csv",dec = ",")
cultivo = data.frame("cultivo"=c(30900,31000,27200,25300,23000,20400,20200,23100,24500,23100,25500,29400,30500,29400))

#Limpiaza de datos
secuestro = df[c(2,13,24),]
rm(df)
rownames(secuestro)=NULL
secuestro = secuestro %>%
  column_to_rownames(var="DEPARTAMENTO")
secuestro = data.frame(t(secuestro))
secuestro = secuestro %>%
  rownames_to_column(var="año")
secuestro = secuestro %>%
  mutate(año=gsub("^X","",año))
secuestro$año = as.numeric(secuestro$año)

secuestro = data.frame(secuestro,cultivo)

#plot
font_add_google("Abril Fatface", "font")
showtext_auto()

ggplot(data=secuestro) +
  
  geom_line(aes(x=año,y=cultivo),color="#588100",size=3)+
  geom_line(aes(x=año,y=COCAÍNA.BASE),color="#71d7d1",size=3)+
  geom_line(aes(x=año,y=CLORHIDRATO.DE.COCAÍNA.),color="#3e8c99",size=3)+
  
  geom_label(aes(x = 2009.85, y = 17000,
                 label = "Cultivos: Hec."),
             stat = "unique",
             size = 8, color = "#fbf2e3",fill="#588100",family="font")+ 
  geom_label(aes(x = 2009.91, y = 15000,
                 label = "Pasta base: Kg."),
             stat = "unique",
             size = 8, color = "#fbf2e3",fill="#71d7d1",family="font")+ 
  geom_label(aes(x = 2010, y = 13000,
                 label = "Clorhidrato: Kg."),
             stat = "unique",
             size = 8, color = "#fbf2e3",fill="#3e8c99",family="font")+ 
  
  geom_fontawesome("fa-arrows-v",x = 2019.3, y = 17800, size = 20,color = "#ff0000") +
  annotate("text", x = 2019.3, y = 20000, label = "mas cultivos", color = "#ff0000",size=7,fontface=2,alpha=1,family="font")+
  annotate("text", x = 2019.3, y = 15500, label = "menos control", color = "#ff0000",size=7,fontface=2,alpha=1,family="font")+
  geom_point(x = 2019.3, y = 16600, size = 275, color = "#ff0000",alpha=.002,shape=16) +
  
  labs(x = "", y = "Kilogramos/Hectarias", caption = "FUENTE: INE Bolivia, FELCN, UNODC. \n@soy_fode", title = "Cocaina Incautada y Cultivos de Coca: \nBOLIVIA") +
  scale_x_continuous(breaks = seq(min(secuestro$año), max(secuestro$año), by = 1)) +
  scale_y_continuous(breaks = seq(1000, 32000, by = 5000)) +
  theme_tufte() +
  theme(
    text = element_text(family = "font", size = 13, color = "#3D5D95"),
    plot.title = element_text(hjust = .55, vjust = -4, color = "#3D5D95", face = "bold", size = 50),
    plot.margin = margin(-10, 40, 20, 40, unit = "pt"),
    axis.title.x = element_text(color = "#3D5D95",face = "bold"),
    axis.title.y = element_text(color = "#3D5D95",face="bold",size=14),
    axis.text.x = element_text(color = "#3D5D95",size = 17,face="bold"),
    axis.text.y = element_text(color = "#3D5D95",size = 17,face="bold"),
    plot.caption = element_text(size = 10, hjust = 0.5, vjust = -5,color="#fbf2e3"),
    panel.border = element_rect(color = "#3D5D95", fill = NA, size =0),
    plot.background = element_rect(colour = "#3D5D95", fill="#fbf2e3", size=30),
    panel.grid.major = element_line(color = "#3d5d95", linetype = "dashed"),
    panel.grid.minor = element_blank(),
    axis.line = element_line(color = "#3D5D95"),
    axis.ticks = element_line(color = "#3D5D95")
  ) 

#ingles
ggplot(data=secuestro) +
  
  geom_line(aes(x=año,y=cultivo),color="#588100",size=3)+
  geom_line(aes(x=año,y=COCAÍNA.BASE),color="#71d7d1",size=3)+
  geom_line(aes(x=año,y=CLORHIDRATO.DE.COCAÍNA.),color="#3e8c99",size=3)+
  
  geom_label(aes(x = 2009.7, y = 17000,
                 label = "Crops: Hec."),
             stat = "unique",
             size = 8, color = "#fbf2e3",fill="#588100",family="font")+ 
  geom_label(aes(x = 2009.9, y = 15000,
                 label = "Base Paste: Kg."),
             stat = "unique",
             size = 8, color = "#fbf2e3",fill="#71d7d1",family="font")+ 
  geom_label(aes(x = 2010.15, y = 13000,
                 label = "Hydrochloride: Kg."),
             stat = "unique",
             size = 8, color = "#fbf2e3",fill="#3e8c99",family="font")+ 
  
  geom_fontawesome("fa-arrows-v",x = 2019.3, y = 17800, size = 20,color = "#ff0000") +
  annotate("text", x = 2019.3, y = 20000, label = "more crops", color = "#ff0000",size=7,fontface=2,alpha=1,family="font")+
  annotate("text", x = 2019.3, y = 15500, label = "less control", color = "#ff0000",size=7,fontface=2,alpha=1,family="font")+
  geom_point(x = 2019.3, y = 16600, size = 275, color = "#ff0000",alpha=.002,shape=16) +
  
  labs(x = "", y = "Kilograms/Hectares ", caption = "Source: INE Bolivia, FELCN, UNODC. \n@soy_fode", title = "Seized Cocaine and Coca Crops: \nBOLIVIA") +
  scale_x_continuous(breaks = seq(min(secuestro$año), max(secuestro$año), by = 1)) +
  scale_y_continuous(breaks = seq(1000, 32000, by = 5000)) +
  theme_tufte() +
  theme(
    text = element_text(family = "font", size = 13, color = "#3D5D95"),
    plot.title = element_text(hjust = .55, vjust = -4, color = "#3D5D95", face = "bold", size = 50),
    plot.margin = margin(-10, 40, 20, 40, unit = "pt"),
    axis.title.x = element_text(color = "#3D5D95",face = "bold"),
    axis.title.y = element_text(color = "#3D5D95",face="bold",size=14),
    axis.text.x = element_text(color = "#3D5D95",size = 17,face="bold"),
    axis.text.y = element_text(color = "#3D5D95",size = 17,face="bold"),
    plot.caption = element_text(size = 10, hjust = 0.5, vjust = -5,color="#fbf2e3"),
    panel.border = element_rect(color = "#3D5D95", fill = NA, size =0),
    plot.background = element_rect(colour = "#3D5D95", fill="#fbf2e3", size=30),
    panel.grid.major = element_line(color = "#3d5d95", linetype = "dashed"),
    panel.grid.minor = element_blank(),
    axis.line = element_line(color = "#3D5D95"),
    axis.ticks = element_line(color = "#3D5D95")
  ) 
