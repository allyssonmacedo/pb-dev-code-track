## Faça um programa que tenha uma função chamada contador (), que receba três parâmetros: inicio, fim e passo e realize a contagem.
# seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 e, 1
#b) de 10 até 0, de 2 em 2
#c) Uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
         passo *= -1
    if passo == 1:
         passo = 1
    print('-' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    
    if inicio < fim:
          cont = inicio
          while cont <= fim:
              print(f'{cont} ', end = '', flush = True)
              sleep(0.2)
              cont += passo
          print('FIM')
    else:
          cont = inicio
          while cont >= fim:
              print(f'{cont} ', end = '', flush = True)
              sleep(0.2)
              cont -= passo
          print('Fim')
         

# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('-' * 20)
print('Agora é a sua vez de personalizar a contagem: ')
in_inicio = int(input('Início: '))
in_fim = int(input('Fim: '))
in_passo = int(input('Passo: '))

contador(in_inicio, in_fim, in_passo)              