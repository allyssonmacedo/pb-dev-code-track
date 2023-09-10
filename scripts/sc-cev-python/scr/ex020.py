#Sorteio entree trabalhos de alunos. faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

#n1 = str(input('Aluno 1: '))
#n2 = str(input('Aluno 2: '))
#n3 = str(input('Aluno 3: '))
#n4 = str(input('Aluno 4: '))
#lista = [n1, n2, n3, n4]
#random.shuffle(lista)
#print(lista)

import itertools

#print(itertools.combinations_with_replacement('abcdef',3))

#random.choices(a: 10)

a = 'a'
b = 'b'
c = 'c'
d = 'd'
e = 'e'
f = 'f'
lista = [a, b, c, d, e, f, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
n2 = random.choices(lista, k=64)
print(''.join(n2))