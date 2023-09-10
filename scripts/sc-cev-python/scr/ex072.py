# Crie um programa qu tenha uma tupla totalmente preencida com uma contagem por extenso, de zero até 10.

# Seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo por extenso

num = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
digitar_numero = []

while digitar_numero not in range(0, 10):
    digitar_numero = int(input('Digite um número entre 0 a 10: '))

print(f'Você digitou {num[digitar_numero]}')