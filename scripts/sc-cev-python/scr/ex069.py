# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá peguntar se o usuário quer ou não continuar. No final, mostre: A - Quantas pessoas tem mais de 18 anos, B - Quantos homens foram cadastrados, C - Quantas mulheres tem menos de 20 anos.

cont_p18 = cont_h = cont_m20 = 0

while True:
    print('-----CADASTRE UMA PESSOA-----')
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o Sexo [M/F] ')).strip().upper()[0]
    if idade > 18: cont_p18 += 1
    if sexo == 'M': cont_h += 1
    if sexo == 'F' and idade < 20: cont_m20 += 1
    parar = ' '
    while parar not in 'SN':
        parar = str(input('Deseja parar? [S/N] ')).strip().upper()[0]
    if parar == 'S':
        break

print(f'''
Você digitou {cont_p18} pessoas com mais de 18 anos \n 
Você digitou {cont_h} pessoas do sexo Masculino \n
Você digitou {cont_m20} pessoas do sexo Feminino que possuem menos de 20 anos''')