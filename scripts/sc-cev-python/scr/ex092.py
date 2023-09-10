# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

import time, datetime
dados = {}
year_retirement = 60

dados['person_name'] = str(input('Digite o seu nome : '))
year_birth = int(input('Digite o ano de nascimento: '))
dados['work_id'] = str(input('Digite o número da carteira de trabalho (se não tiver deixe vazio): '))

current_year = datetime.datetime.now().year
dados['age']  = current_year - year_birth

if dados['work_id'] != '':
    dados['year_contract'] = int(input('Digite o ano da primeira contratação : '))
    dados['salary'] = float(input('Qual o seu salário mensal ? '))

print(f"{dados['person_name']} possui {dados['age']} e vai se aposentar em {60-dados['age']} anos")


