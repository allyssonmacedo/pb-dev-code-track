# Faça um programa que leia o nome e idade de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) quantas pessoas foram cadastradas
# b) Uma listagem com as pessoas mais velhas
# c) uma listagem com as pessoas mais novas



list_users = []

while True:
    name = str(input('Digite o nome da pessoa: '))
    age = int(input('Digite a idade da pessoa [anos]: '))
    user = [name, age]
    list_users.append(user)
    add_new = str(input('Deseja adicionar uma outra pessoa ? [S/N] '))
    if add_new in 'Nn':
        break
#A)
qtd_users = len(list_users)
print(f'Foram cadastradas {qtd_users} usuários')

# B e C)
age_list = []
for item in range(0, len(list_users)):
    age_item = list_users[item][1]
    age_list.append(age_item)

couter = 0

def fmax_min_age (max_min, maior_menor):
    max_min_age = max_min(age_list)
    for item in range(0, len(list_users)):
        if max_min(age_list) == list_users[item][1]:
            print(f'{list_users[item][0]} possui a {maior_menor} idade ({list_users[item][1]})')


fmax_min_age(max, 'maior')
fmax_min_age(min, 'menor')
    
