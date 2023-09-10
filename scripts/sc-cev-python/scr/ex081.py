# crie um programa que vai ler vários números e colocar em uma lista.
# depois disso, mostre:
# a) quantos números foram digitados.
# b) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

list = []

while True:
    val = float(input('Digite um valor: '))
    list.append(val)
    cont = input('Deseja continuar ? [S/N]: ')
    if cont in 'Nn':
        break
print(f'Você digitou {len(list)}')
print(f'Você digitou os valores (em ordem decrescente):')
print(sorted(list, reverse=True))

if 5 in list: print('O valor 5 foi digitado e está na lista') 
else: print('O valor 5 não foi digitado')