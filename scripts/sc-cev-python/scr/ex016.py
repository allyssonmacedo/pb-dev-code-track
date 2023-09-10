#Crie um programa que leie a parte inteira de um número (arredondar para baixo)


import math
n = float((input('Digite o número')))
num = math.ceil(n)
num2 = math.floor(n)

print('Seu número é {}, arredondando para baixo é {} e para cima {}'.format(n, num2, num))

#Outra forma

from math import trunc
n2 = float(input('Digite um número.')) 
print('O número digitado foi {} e a porção inteira do número é {}'.format(n2, trunc(n2)))