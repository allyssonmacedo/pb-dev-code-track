#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base da conversão:
#1 para binário
#2 para octal
#3 para hexadecimal


num = int(input('Digite um número inteiro: '))
print(""""Escolha uma das bases para conversão:
[1] converter para Binário
[2] converter para Octal
[3] converter para Hexadecimal """)
escolha = int(input('Sua opção: '))
if escolha == 1:
    print(f'{num} convertido para Binário é igual a {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para Binário é igual a {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para Binário é igual a {hex(num)[2:]}')
else:
    print('Opção inválida')