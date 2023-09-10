# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar no final, mostre:  A - Qual é o total gasto na compra, B - Quantos produtos custam mais de R$ 1000, C - Qual é o nome do produto mais barato.

total_compra = produtos_caros = produtos = 0
prod_mais_barato = ' '

while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    produtos += 1

    if produtos == 1:
           menor = preço
    else:
        if preço < menor:
            prod_mais_barato = nome

    if preço > 1000: produtos_caros += 1
    total_compra += preço

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [S/N] ')).strip().upper()[0]
    if continuar == 'N': break

print(f'''
Você digitou {produtos} produtos \n 
O total da compra foi de R$ {total_compra} \n
Você comprou {produtos_caros} produtos com valor acima de R$ 1.000,00 \n
O produto mais barato foi {prod_mais_barato}''')