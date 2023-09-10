#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

contador = 0
for c in range(1,8):
    ano = int(input(f'Em que ano nasceu a {c} pessoa? '))
    idade = datetime.datetime.today().year - ano

    if idade >= 18:
        contador += 1
print(f'{contador} das 7 pessoas são maiores de idade e {7 - contador} são menores de idade')
