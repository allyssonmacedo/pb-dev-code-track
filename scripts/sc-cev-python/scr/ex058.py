# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

num = random.randint(0,10)
contador = 0

while True:
    global modo
    modo = int(input("""Deseja jogar com ou sem dicas?: 
    [1] Sem dicas
    [2] Com dicas
    """))
    if modo == 1 or modo == 2:
        break

if modo == 1:
    while True:
        num = random.randint(0,10)
        tentativa = int(input('Digite um valor inteiro entre 0 a 10 e veja se acertou: '))

        if tentativa == num:
            print(f'Parabéns, você acertou. O número é {num}')
            break
        
        else:
            print(f'Você errou, o número que eu estava pensando era {num}')
            contador += 1
    print(f'Você ganhou!. Você jogou {contador + 1} vezes até acertar')

if modo == 2:
    while True:
        tentativa = int(input('Digite um valor inteiro entre 0 a 10 e veja se acertou: '))

        if tentativa == num:
            print(f'Parabéns, você acertou. O número é {num}')
            break
        
        else:
            contador += 1
            if num > tentativa:
                print('Mais... Tente novamente')
            if num < tentativa:
                print('Menos... tente novamente')

    print(f'Você ganhou!. Você jogou {contador + 1} vezes até acertar')


