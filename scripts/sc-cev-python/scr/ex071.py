# Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs: considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1 ##

import time

print('Caixa eletrônico')

valor = int(input('Qual o valor deseja sacar? '))
c50 = c20 = c10 = c01 = 0

while True:
    if valor >= 50:
        c50 = valor // 50 
        troco = valor % 50
    if troco >= 20:
        c20 = troco // 20
        troco = troco % 20
    if troco >= 10:
        c10 = troco // 10
        troco = troco % 10
    else:
        c01 = troco
        break
print('contando cédulas...')
time.sleep(1.5)
print(f'''
Você solicitou um saque de R$ {valor},00 e você irá obter:
{c50:.0f} notas de R$ 50,00
{c20:.0f} notas de R$ 20,00
{c10:.0f} notas de R$ 10,00 
{c01:.0f} notas de R$ 1,00
      ''')
    
        