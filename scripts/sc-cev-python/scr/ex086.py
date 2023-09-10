# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
# No final, mostre a matriz na tabela com a formatação correta.

print('Opa, tudo bem?? Iremos fazer uma matriz 3x3, conforme o modelo abaixo')
matrix = '''
[], [], [],
[], [], [],
[], [], []'''

print(matrix)

print('Agora digite os números que deseja visualizar seguindo a ordem da direita para a esquerda')

counter = 1
numeros = []
for num in range(9):
    num = int(input(f'digite o {counter}º número: '))
    numeros.append(num)
    counter += 1

print('Você digitou a matriz abaixo: ')

matrix_add = f'''
[{numeros[0]}], [{numeros[1]}], [{numeros[2]}],
[{numeros[3]}], [{numeros[4]}], [{numeros[5]}],
[{numeros[6]}], [{numeros[7]}], [{numeros[8]}]'''

print(matrix_add)

# Resolução aula:

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range (0, 3):
#     for c in range(0,3):
#         matriz[l][c] = int(input(f'Digite u valor para [{l}, {c}]: '))
# print('-= * 30')
# for l in range (0,3):
#     for c in range(0,3):
#         print(f'[{matriz[l][c]:^5}]', end = '')
#     print()