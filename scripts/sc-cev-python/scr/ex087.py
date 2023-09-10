# Aprimore o desafio anterior, mostrando no final 
# A) A soma de todos os valores pares digitados

# b) A soma dos valores da terceira coluna

# c) O maior valor da segunda linha

import ex086

par = []
for item in ex086.numeros:
    if item % 2 == 0:
        par.append(item)

print(f'A soma de todos os valores pares é de {sum(par)}')

# Os valores da terceira coluna são aqueles em que o resto da divisão por 3 é igual a dois (2, 5, 8):]
third_col = []
for item in ex086.numeros:
    if ex086.numeros.index(item) % 3 == 2:
        third_col.append(item)

print(f'A soma de todos os valores da terceira coluna é de {sum(third_col)}')

# Os valores da segunda linha são aqueles em que o índice é entre 3 a 5:
second_row = []
for item in ex086.numeros:
    if ex086.numeros.index(item) in [3,4,5]:
        second_row.append(item)

print(f'O máximo valor da segunda linha é {max(second_row)}')






