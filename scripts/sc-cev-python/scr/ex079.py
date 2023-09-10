# crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


list = []

while True:
    val = float(input('Digite um valor: '))
    if val not in list:
        list.append(val)
    cont = input('Deseja continuar ? [S/N]: ')
    if cont in 'Nn':
        break
print(f'Você digitou os valores (em ordem crescente):')
print(sorted(list))
