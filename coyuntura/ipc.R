#Library
library(tidyverse)
library(ggplot2)
library(ggthemes)
library(showtext)
library(emojifont)
library(fontawesome)
library(ggfortify)
library(readxl)

#data
indice.mensual = read_excel("data/ipc.xlsx",sheet = "ÍNDICE MENSUAL")
indice.mensual = indice.mensual[-13,-1] 
indice.mensual <- unlist(indice.mensual[, c("2018",
                                           "2019",
                                           "2020",
                                           "2021",
                                           "2022", 
                                           "2023")])

var.mensual = read_excel("data/ipc.xlsx",sheet = "VAR MENSUAL")
var.mensual = var.mensual[-c(13,14),-1]
var.mensual <- unlist(var.mensual[, c("2018",
                                           "2019",
                                           "2020",
                                           "2021",
                                           "2022", 
                                           "2023")])

var.acumulada = read_excel("data/ipc.xlsx",sheet = "VAR ACUMULADA")
var.acumulada <- unlist(var.acumulada[, c("2018",
                                           "2019",
                                           "2020",
                                           "2021",
                                           "2022", 
                                           "2023")])

'"
Es la variación promedio de los precios entre el mes de referencia y el mismo 
mes del año inmediatamente anterior, según la siguiente fórmula:
Variación (%) 12 meses t = [(IPCmes t ⁄ IPCmes t, año anterior) -1]*100.
"'
var.12.meses = read_excel("data/ipc.xlsx",sheet = "VAR 12 MESES")
var.12.meses <- unlist(var.12.meses[, c("2018",
                                           "2019",
                                           "2020",
                                           "2021",
                                           "2022", 
                                           "2023")])

ipc = data.frame(var.mensual,var.acumulada,var.12.meses)
ipc = ts(ipc,start = c(2018,1),end = c(2023,5),frequency = 12)
rm(indice.mensual)
rm(var.12.meses)
rm(var.acumulada)
rm(var.mensual)


ipc <- fortify(ipc)

font_add_google("Abril Fatface", "font")
showtext_auto()

ggplot(ipc, aes(x = Index)) +
  
  geom_line(aes(y = var.12.meses), color = "red", size = 1) +
  geom_bar(aes(y = var.acumulada), stat = "identity", fill = "#bea3d9",alpha=0.7) +
  geom_ribbon(aes(ymin = var.12.meses, ymax = 0), fill = "#dddef1", alpha = 0.15) +
  geom_line(aes(y = var.mensual), color = "#7ab7db",size=1.2) +
  
  geom_label(aes(x = as.Date("2019-2-01",format="%Y-%m-%d"), y = 2.5,
                 label = "Variación a 12 meses"),
             stat = "unique",
             size = 8, color = "#dddef1",fill="red",family="font",alpha=0.8)+ 
  
  geom_label(aes(x = as.Date("2018-03-01",format="%Y-%m-%d"), y = 1,
                 label = "Variación Acum."),
             stat = "unique",
             size = 8, color = "#dddef1",fill="#bea3d9",family="font")+ 
  
  geom_label(aes(x = as.Date("2018-7-01",format="%Y-%m-%d"), y = -.5,
                 label = "Variación Mensual"),
             stat = "unique",
             size = 8, color = "#dddef1",fill="#7ab7db",family="font")+ 
  
  labs(x = "", y = "", caption = "FUENTE: INE Bolivia. \n@soy_fode", title = "IPC mensual: BOLIVIA") +
  
  scale_x_date(date_labels = "%m-%Y", date_breaks = "1 month") +
  
  theme_tufte() +
  
  theme(
    text = element_text(family = "font", size = 13, color = "#7ab7db"),
    plot.title = element_text(hjust = .7, vjust = -4, color = "#7ab7db", face = "bold", size = 50),
    plot.margin = margin(-10, 40, 20, 40, unit = "pt"),
    axis.title.x = element_text(color = "#7ab7db",face = "bold"),
    axis.title.y = element_text(color = "#7ab7db",face="bold",size=14),
    axis.text.x = element_text(color = "#dddef1",size = 12,face="bold",angle=45,vjust = 1,hjust = 1),
    axis.text.y = element_text(color = "#dddef1",size = 12,face="bold"),
    plot.caption = element_text(size = 10, hjust = 0.5, vjust = -5,color="#dddef1"),
    panel.border = element_rect(color = "#313a79", fill = NA, size =0),
    plot.background = element_rect(colour = "#313a79", fill="#313a79", size=30),
    panel.grid.major = element_line(color = "#3d5d95", linetype = "dashed"),
    panel.grid.minor = element_blank(),
    axis.line = element_line(color = "#7ab7db"),
    axis.ticks = element_line(color = "#7ab7db")
  ) 

  
