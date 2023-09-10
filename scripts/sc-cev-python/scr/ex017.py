#Faça um programa que leia o comprimento os catetos opostos e adjacentes e calcule e mostre o comprimento da hipotenusa.

import math

cat1 = float(input('Digite o cateto 1: '))
cat2 = float(input('Digite o cateto 2: '))
h = math.hypot(cat1, cat2)

print('A hipotenusa do seu triângulos de lados {} e {} é {}!'.format(cat1, cat2, h))