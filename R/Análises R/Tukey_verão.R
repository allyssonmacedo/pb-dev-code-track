ver?o <- read.csv("E:/Allysson/Acessar/Universidade/PIBIC 2019-2020/Experimentos/Ver?o/Estatistica_Ver?o_Fisicoquimica.csv", header = TRUE)
View(ver?o)
options(OutDec = ",")

bartlett.test(ver?o$VITC~ver?o$TRAT) # Realiza o teste de Bartlett (Homogeneidade)


shapiro.test(ver?o$VITC) # Realiza o teste de Shapiro-Wilk (Normalidade)

library(ExpDes.pt) # Libera o pacote ExpDes.pt
dic(ver?o$TRAT, # Tratamentos
    ver?o$VITC, # Vari?vel resposta
    quali = TRUE, # Define que s?o tratamentos qualitativos
    mcomp = "tukey", # Define o teste de compara??o de m?dias
    sigT = 0.05, # Define o nivel de signific?ncia do teste para m?dias
    sigF = 0.05 # Define o nivel de signific?ncia do teste F 
)

#boxplot(primavera$PESO ~primavera$TRAT, # Define os dados a serem utilizados
        xlab="Tratamentos", # Adiciona um r?tulo ao eixo x
        ylab="Peso(g)", # Adiciona um r?tulo para o eixo y
        ylim=c(0,3000), # Define os limites do eixo y
        #col=c("salmon1","darkseagreen1","lightskyblue2", # Define a cor interna das caixas
        #border=c("black"), # Define a cor da borda da caixa
        #cex.lab=1.4, # Define o tamanho dos rotulos dos eixos
        #las= # Define o direcionamento dos valores dos eixos (1 = todos horizontais)
)