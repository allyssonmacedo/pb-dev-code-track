#Análise Fatorial
library(clipr) #install.packages("clipr")
library(ExpDes.pt) #install.packages("ExpDes.pt")

#Fatorial DIC
#Definir o diretório do arquivo e dados
#D1 <- read.csv("E:/Allysson/Acessar/Universidade/PIBIC 2019-2020/Experimentos/Dados_Fatorial_Intera??o.csv", header = TRUE)
#D1 <- read.table("clipboard", sep="", header=T, dec=",", row.names=1)
D1 <- read.table("clipboard", header = T)
View(D1)
# dim(D1) -- retorna número de linhas e colunas
head(D1) # retorna o cabeçalho -- usar para visualizar o cabeçalho para preencher abaixo
attach(D1)

#Análise Fatorial
fat2.dic(D1$Meses, D1$tanque, D1$cbt, quali = c(TRUE, TRUE), mcomp = "tukey", fac.names = c("CBT (*1000 UFC/Ml)", "ccs (*1000 células/mL)"), 
         sigT = 0.05, sigF = 0.05)

#Anova para descobrir os GL e os SQ


dic(D1$Concentra??o, # Tratamentos
    D1$MORT, # Vari?vel resposta
    quali = TRUE, # Define que s?o tratamentos qualitativos
    mcomp = "tukey", # Define o teste de compara??o de m?dias
    sigT = 0.05, # Define o nivel de signific?ncia do teste para m?dias
    sigF = 0.05 # Define o nivel de signific?ncia do teste F 
)


#Fits sequencial regression models until the third power.
#reg.poly(Resposta, Tratamentos, GL error, SQ error, GL trat, SQ trat)
reg.poly(D1$MORT, D1$Concentra??o, 190, 377261, 4, 7829)


____________________________________


#Prepara??o dos dados
x = with(df,Concentra??o)
y = with(df, X24)
tamanho = dim(df)
grafico = seq(min(x),max(x), #length.out = tamanho
              )

#scatterplot com regress?o
plot(y~x, data=df, xlab = "Concentra??o (ppm)",
     ylab = "Mortalidade 24h (%)")

#Ajuste reta de regress?o (Linear)
modelo = lm(y~x, data = df)
abline(modelo, lty=2, lwd=2,col = "blue")
modelo

#Ajuste regress?o quadrada #Caso queira outro polinomio s? alterar
modelo.1 = lm(y~poly(x,2))
modelo.1

#Scatterplot com ajuste polinominal
plot(y~x, data=df, xlab = "Concentra??o (ppm)",
     ylab = "Mortalidade 12h (%)")
abline(modelo, lty = 2, lwd = 2, col = "red")  
lines(grafico, predict(modelo.1, data.frame(x=grafico)),
      col="blue", lty=2, lwd=2)

