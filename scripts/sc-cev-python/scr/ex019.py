# Um professor quer sortear um dos seus quatro alunos para apagar um quadro.
# Faça um programa que ajuda ele, lendo o nome delas e escrevendo o nome do escolhido

import random

sorteio = random.randint(1, 4)

if sorteio == 1:
    print('João')
if sorteio == 2:
    print('Marta')
if sorteio == 3:
    print('Miguel')
if sorteio == 4:
    print('Gabriel')    

#Outro modo:
n1 = str(input('aluno1: '))
n2 = str(input('aluno2: '))
n3 = str(input('aluno3: '))
n4 = str(input('aluno4: '))
lista = [n1, n2, n3, n4]
print(random.choice(lista))