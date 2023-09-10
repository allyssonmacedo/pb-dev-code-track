#Crie um programa que mostre se o número digitado é par ou impar

try:
    num = int(input('Digite um número inteiro: '))
    if (num % 2) == 0:
        print('O número é par')
    else:
        print('O número é impar')
except:
    print('você digitou algo errado, tente novamente')
