# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

import random

n1 =  random.randint(1,10)
n2 =  random.randint(1,10)
n3 =  random.randint(1,10)
n4 =  random.randint(1,10)
n5 =  random.randint(1,10)

tuple = (n1, n2, n3, n4, n5)
print(tuple)
print(f' o menor valor é {min(tuple)}' )
print(f' o maior valor é {max(tuple)}' )