##faça um programa que leia um número inteiro e diga se ele é ou não um número primo
vezes = 0
num = int(input('Digite o número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end=' ')
        vezes += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end =' ')
if vezes == 2:
    print('\n\033[m O número é primo')
else:
    print(f'\n\033[m O número {num} não é primo e possui {vezes} divisores')