# Crie um programa onde o usuário possa digitar sete valores núericos e cadastre-os em uma lista única que mantenha separado os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

counter = 1
list_value = [[],[]]

while counter <= 7:
    input_value = int(input('Digite um valor inteiro: '))
    if input_value % 2 == 0:
        list_value[0].append(input_value)
    else: 
        list_value[1].append(input_value)
    counter += 1

par_sort = sorted(list_value[0])
ímpar_sort = sorted(list_value[1])

print(f'A lista par é {par_sort}')
print(f'A lista ímpar é {ímpar_sort}')


