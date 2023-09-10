#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] menor
#[4] novos numeros
#[5] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso
import time
import numpy as np

num_1 = float(input('Digite o primeiro valor: '))
num_2 = float(input('Digite o segundo valor: '))
operacao = 0

while operacao !=5:
    print('Qual operação você deseja realizar? ')
    operacao = int(input(""" 
    [1] somar
    [2] multiplicar
    [3] menor
    [4] novos numeros
    [5] sair do programa 
    """))
    if operacao == 1:
        resultado = num_1 + num_2
        print(resultado)
    elif operacao == 2:
        resultado = num_1 * num_2
        print(resultado)
    elif operacao == 3:
        resultado = np.min([num_1, num_2])
        print(resultado)
    elif operacao == 4:
        num_1 = float(input('Digite o primeiro número: '))
        num_2 = float(input('Digite o segundo número: '))
    elif operacao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    time.sleep(2)
print('Programa finalizado')