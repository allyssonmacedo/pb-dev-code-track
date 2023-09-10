#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas minúsculas
# Quantas letras ao todo sem considerar espaços)
#Quantas letras tem o primeiro nome


nome = input('Digite o seu nome completo: ')

print(f'O nome completo em minúsculo é {nome.lower()} \n')
print(f'O nome completo em MAIÚSCULO é {nome.upper()} \n')
print(f'O nome completo em minúsculo é {nome.lower()} \n')

sem_espaco = nome.replace(' ','')
print(f'tamanho sem espaço: {len(sem_espaco)}')

dividido = nome.split()
print(dividido)

qt_primeiro_nome = len(dividido[0])

print(qt_primeiro_nome)