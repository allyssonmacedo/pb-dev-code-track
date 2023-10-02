

# # x = datetime.now() - timedelta(days= 30)

# # print(x.month)

# import datetime

# d1 = datetime.datetime(2023,8,16)
# d2 = datetime.datetime(2023,8,13)
# #d2 = datetime.datetime.now()

# diff = d2 - d1

# days = diff.days
# years, days = days // 365, days % 365
# months, days = days // 30, days % 30

# seconds = diff.seconds
# hours, seconds = seconds // 3600, seconds % 3600
# minutes, seconds = seconds // 60, seconds % 60

# print("Desde {} passaram {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos".format(d1, years, months, days, hours, minutes, seconds))

# import pandas as pd

# # Criando um dicionário com os dados dos filmes alugados
# dados = {
#     'Título do Filme': ['Filme 1', 'Filme 2', 'Filme 3', 'Filme 4'],
#     'Data de Contratação': ['2023-09-15', '2023-09-20', '2023-09-10', '2023-09-25'],
#     'Data de Devolução': ['2023-10-18', '2023-10-25', '2023-10-14', '2023-10-28']
# }

# # Criando um DataFrame a partir do dicionário
# df = pd.DataFrame(dados)

# # Convertendo as colunas de data para o tipo datetime
# df['Data de Contratação'] = pd.to_datetime(df['Data de Contratação'])
# df['Data de Devolução'] = pd.to_datetime(df['Data de Devolução'])

# # Calculando a duração da locação em meses
# df['Duração da Locação (em meses)'] = (df['Data de Devolução'].dt.to_period('M') - df['Data de Contratação'].dt.to_period('M')).ne

# # Exibindo o DataFrame
# print(df)
##############################



from datetime import datetime
from dateutil.relativedelta import relativedelta

d1 = datetime(2023, 7, 16, 23)
d2 = datetime(2024, 9, 10, 17)
# diferença entre d1 e d2
diff = relativedelta(d2, d1)
print("{} anos, {} meses, {} dias, {} horas, {} minutos, {} segundos"
       .format(diff.years, diff.months, diff.days, diff.hours, diff.minutes, diff.seconds))
# a partir do Python 3.6, é possível usar f-strings
print(f"{diff.years} anos, {diff.months} meses, {diff.days} dias, {diff.hours} horas, {diff.minutes} minutos, {diff.seconds} segundos")

print(diff)


#############################

import pandas as pd
from dateutil import relativedelta

# Criando um dicionário com os dados dos filmes alugados
dados = {
    'Título do Filme': ['Filme 1', 'Filme 2', 'Filme 3', 'Filme 4'],
    'Data de Contratação': ['2023-07-16', '2023-09-20', '2023-09-10', '2023-09-25'],
    'Data de Devolução': ['2007-09-10', '2023-05-25', '2023-09-14', '2023-10-28']
}

# Criando um DataFrame a partir do dicionário
df = pd.DataFrame(dados)

# Convertendo as colunas de data para o tipo datetime
df['Data de Contratação'] = pd.to_datetime(df['Data de Contratação'])
df['Data de Devolução'] = pd.to_datetime(df['Data de Devolução'])

# Calculando a duração da locação em meses
df['Duração da Locação (em meses)'] = df.apply(lambda row: relativedelta.relativedelta(row['Data de Devolução'], row['Data de Contratação']).months, axis=1)

# Exibindo o DataFrame
print(df)