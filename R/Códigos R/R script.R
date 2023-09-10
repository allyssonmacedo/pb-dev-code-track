install.packages("clipr")
library("clipr")
meusdados <- read_clip_tbl()
View(meusdados)
str(meusdados)

install.packages("psych") #pacote para fazer análise fatorial
library("psych") #liberar o pacote para utilização 

describe (meusdados) #média (mean), desvio padrão (sd), mínimo (min) e máximo (max), e os dados de simetria (skew) e o tamanho das caudas (kurtosis)

dados <- read_clip_tbl()
View(dados)
corelação <- cor(dados) #cria uma nova variável (correlação) e realiza a corelação dos dados
LowCor(dados)
#Link que pode ser útil: https://medium.com/psicodata/tutorial-de-analise-fatorial-exploratoria-no-r-1db5b6bf8dd5

# Pacote do Agro: https://github.com/AgronomiaR/AgroR

is.factor(Estação)

install.packages("AgroR")
library("AgroR")

fat2.dic(meusdados$Estádio, meusdados$Estação, meusdados$Peso, quali = c(TRUE, TRUE), mcomp = "tukey", fac.names = c("Est?dios fenol?gicos", "Esta??o"), 
         sigT = 0.05, sigF = 0.05)


bartlett.test(meusdados$Peso~meusdados$TRAT) # Realiza o teste de Bartlett (Homogeneidade)
    
