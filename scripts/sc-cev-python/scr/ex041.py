#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostra a sua categoria, de acordo com a idade:
#Até 9 anos: mirin ; até 14: infantil ;  até 19 anos: Junior ; Até 25 anos : Sênior ; Acima : Master

import datetime

ano_nasc = int(input('Em que ano você nasceu? '))
idade = datetime.datetime.today().year - ano_nasc
print(f'Sua idade é {idade}')

if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('Categoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade <= 25:
    print('Categoria Sênior')
elif idade > 25:
    print('Categoria Master')
