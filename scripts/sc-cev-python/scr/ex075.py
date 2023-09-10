# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre
# a) Quantas vezes apareceu o valor 9
# b) Em que posição foi digitado o primeiro valor 3
# c) Quais foram os números pares

v1 = int(input('Digite o primeiro valor '))
v2 = int(input('Digite o segundo valor '))
v3 = int(input('Digite o terceiro valor '))
v4 = int(input('Digite o quarto valor '))

núm = (v1, v2, v3, v4)

print(f'Você digitou os números {núm}')
print(f'O valor 9 apareceu {núm.count(9)}')
if 3 in núm:
    print(f'O número 3 apareceu {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end = '')

for n in núm:
    if n % 2 == 0:
        print(n, end=' ')