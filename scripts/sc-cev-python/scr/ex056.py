#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre :
#A média de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres têm menos de 20 anos

import numpy as np

contador_mulher = 0
contador_homem = 0

for p in range(1,5):
    print(f'{"-" * 5} {p}ª PESSOA {"-" * 5}')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('M ou F: ').lower())

    if sexo == 'm':
        contador_homem += 1
        if contador_homem == 1:
            idade_mais_velha = idade
            homem_mais_velho = nome
        else:
            if idade > idade_mais_velha:
                    homem_mais_velho = nome
    
    if sexo == 'f':
        if idade < 20:
            contador_mulher += 1


print (f"""A média de idade é de {np.mean(idade)}
O homem mais velho é {homem_mais_velho}
Há {contador_mulher} mulher(es) com menos de 20 anos""")

