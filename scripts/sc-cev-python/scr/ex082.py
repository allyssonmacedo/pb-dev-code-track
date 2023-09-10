# crie um programa que vai ler vários números e colocar em uma lista
# depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas

list = p_list = i_list = []

while True:
    val = float(input('Digite um valor: '))
    list.append(val)
    cont = input('Deseja continuar ? [S/N]: ')
    if cont in 'Nn':
        break

for item in list:
    if item % 2 == 0: 
        p_list.append(item) 
    else: 
        i_list.append(item)

print(f'Você digitou os valores:')
print(list)
print(p_list)
print(i_list)