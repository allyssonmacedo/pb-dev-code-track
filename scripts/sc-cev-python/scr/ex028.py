#Escreva um programa que faça o computador pensar em número inteiro entre 0 e 5 e peça para o usuário
#descobrir  qual foi o número scolhido pelo computador.

import random

num = random.randint(0,5)

tentativa = int(input('Digite um valor inteiro entre 0 a 5 e veja se acertou: '))

if tentativa == num:
    print(f'Parabéns, você acertou. O número é {num}')
else:
    print(f'Você errou, o número que eu estava pensando era {num}')