#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
#Ex: digite um número: 1834
#Unidade:4
#Dezena: 3 ....

num = int(input('Digite um número entre 0 a 9999: '))

print(f""" Unidade = {num // 1 % 10}""")
print(f""" Dezena = {num // 10 % 10}""")
print(f""" Centena = {num // 100 % 10}""")
print(f""" Unid. Milhar = {num // 1000 % 10}""")