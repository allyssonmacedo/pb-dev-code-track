#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = 'S'
soma = media = count = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    count += 1
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N] ')).upper().strip()[0]
media = soma / count
print(f'Você digitou {count} números e a média entre eles é de {media}')
print(f'O maior número é {maior} e o menor número é {menor}')

