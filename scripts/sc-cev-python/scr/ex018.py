#Faça um programa que leia um ângulo qualquer e mostre na tela o vaalor do seno, cosseno e tangente

import math

an = float(input('Digite um ângulo: '))
cos = math.cos(math.radians(an))
sen = math.sin(math.radians(an))
tan = math.tan(math.radians(an))

print (cos, sen, tan)
