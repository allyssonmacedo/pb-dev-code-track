# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando o dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade do grupo
#C) Uma lista com todas as mulheres
#D) Uma lista com todas as pessoas com idade acima da média

pessoas = []
soma = média = 0

while True:
    nome = str(input('Digite o nome: '))
    while True:
        sexo = str(input('Digite o sexo [M/F]: ')).upper()[0]
        if sexo in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')

    idade = int(input('Digite a idade: '))

    pessoa = {
        'nome': nome,
        'idade': idade,
        'sexo': sexo
    }

    soma += pessoa['idade']

    pessoas.append(pessoa)
    continuar = str(input('Deseja continuar [S/N]: '))
    if continuar in 'nN':
        break

print(f'A) Você digitou {len(pessoas)} pessoas')

média = soma / len(pessoas)

print(f'B) A média de idade das pessoas cadastradas é {média:5.2f}')

# mulheres na lista
print('As mulheres na lista foram: ', end = '')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end = '')
print()

print('D) Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] >= média:
        print('     ', end = '')
        for k,v in p.items():
            print(f'{k} = {v} ', end = '')
        print()
print('<< ENCERRADO >>')