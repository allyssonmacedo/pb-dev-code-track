# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência
#no final , mostre uma listagem de preços, organizando os dados em forma tabular.

listagem = (
    'lapis', 1.75,
    'borracha', 0.8,
    'caderno', 2.4,
    'estojo', 1.25,
    'caneta', 1.5,
    'cola', 3.5
)
print('-' * 40)
print(f'{"Listagem de preços":^40}')
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)