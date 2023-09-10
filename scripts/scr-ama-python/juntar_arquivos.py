import pandas as pd
import openpyxl as xl

print(""""
INSTRUÇÕES DE USO:

O SEGUINTE PROGRAMA IRÁ RETORNAR UMA PLANILHA DE EXCEL APÓS SER INFORMADO 2 PLANILHAS COM UMA COLUNA EM COMUM ENTRE ELAS.
""")
arq_1 = input('Digite o nome do 1º arquivo. Ex: plantio-ipe.xlsx : ')
arq_2 = input('Digite o nome do 2º arquivo. Ex: plantio-caz.xlsx: ')

arquivo_1 = pd.read_excel(arq_1) ###Digitar entre aspas o enderço do arquivo.
id_1 = input('Digite o nome da coluna que será usada para unir com o 2º arquivo: ') ### Coluna em comum do arquivo 1

arquivo_2 = pd.read_excel(arq_2) ###Digitar entre aspas o enderço do arquivo.
id_2 = input('Digite o nome da coluna que será usada para unir com o 1º arquivo: ') ### COluna em comum do arquivo 2

metodo_digito = input("""
Digite o número do metódo de união. \n 
1 - Preservar todas as linhas de ambas as colunas. \n 
2 - Preserva apenas as linhas presentes na 1ª tabela \n 
3 - Preserva apenas as linhas presentes na 2º tabela

Obs: Caso digite um valor inválido, a opção 1 será selecionada.
""")

if metodo_digito == 1:
    metodo = 'outer'
if metodo_digito == 2:
    metodo = 'left'
if metodo_digito == 3:
    metodo = 'right'
else: 
    metodo = 'outer'

##Junta o arquivo 1 e o arquivo 2 com base nos ID's, preservando todas as linhas do arquivo 1.
juntos = pd.merge(left = arquivo_1, right= arquivo_2, left_on = id_1, right_on = id_2, how=metodo)  

#visualização previa dos dados
print('A prévia do arquivo será: ')
print(juntos.head())

#Exportando os dados
nome_arquivo = input('Digite o nome do arquivo que será salvo. Ex: plantio-ipe-caz.xlsx : ')
juntos.to_excel(nome_arquivo) ### exporta o arquivo para excel (na mesma pasta do arquivo)
print('Tudo ok. O arquivo está salvo no diretório')

##Cria o executável
#pyinstaller –onefile nome-do-arquivo.py