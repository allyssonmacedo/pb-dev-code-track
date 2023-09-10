# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interromid quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

cont = 0

print(f'{"*"*10} Jogo do Par ou ímpar {"*"*10}')

while True:
    valor = int(input('Digite um número: '))
    computador = random.randint(1,2)
    resultado = valor + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ').strip().upper()[0])
        print('Digite P para Par ou I para ímpar')
    if tipo == 'P':
        print(f'O computador escolheu {computador}')   
        
        if (resultado % 2 == 0) :
            print('Parabéns, você ganhou')
            cont =+ 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        print(f'O computador escolheu {computador}')
        if (resultado % 2 == 1) :
            print('Parabéns, você ganhou')
            cont =+ 1
        else:
            print('Você perdeu!')
            break
print(f'Voce ganhou {cont} vezes')
