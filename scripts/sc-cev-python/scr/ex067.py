# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solificado for negativo.

while True:
    num = int(input('Digite um número. Digite um valor negativo para parar : '))
    if num > 0:
        print('-'*20)
        print(f'TABUADA DE {num}')
        for item in range(1,10):
            print(f'{item} X {num} = {item*num}')
        print('-'*20)
    elif num == 0:
        print('A múltiplicação de qualquer número por zero resulta em zero')
    elif num < 0:
        print(f'{"*"*20} Fim do programa {"*"*20}')
        break