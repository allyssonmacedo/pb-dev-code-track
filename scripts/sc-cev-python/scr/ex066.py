# Crie um programa que leia vários números inteiros pelo teclado, o programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada, no final mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)

soma = cont = 0

while True:
    num = int(input('Digite o número (999 para parar): '))

    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} números e a soma é {soma}')
