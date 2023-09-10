#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

n = int(input('Qual o número quer visualizar a tabuada?: ')) 
v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('A tabuada para o número escolhido é a seguinte: ')

print('-'*40)
print('{:20} * {} = {:.2f}'.format(n, 1, n*1))
print('{:20} * {} = {:.2f}'.format(n, 2, n*2))
print('{:20}'.format('.....'))
print('{:20} * {} = {:.2f}'.format(n, 9, n*9))
print('-'*40)
