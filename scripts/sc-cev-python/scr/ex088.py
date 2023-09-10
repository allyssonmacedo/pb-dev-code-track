# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

num_jogos = int(input('Digite a quantidade de jogos que deseja formar: '))

num = []

for item in range(num_jogos):
    r_list = []
    while len(r_list) < 6:
        r_number = random.randint(1,60)
        if r_number not in r_list:
            r_list.append(r_number)
    num.append(r_list)

for i, l in enumerate(num):
    print(f'Jogo {i+1}: {l}')

print('-=' * 5, 'BOA SORTE', '-=' *5)

        
    