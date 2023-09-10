# faça um programa que leia os 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

list = []
for val in range(5):
    val = float(input("DIGITE UM NÚMERO: "))
    list.append(val)
print(f" você digitou a lista \n {list}")
print(f"O maior valor digitado foi {max(list)} e o menor valor digitado foi {min(list)} nas posições {list.index(max(list)) + 1} e {list.index(min(list)) + 1} respectivamente")

# for i, v in enumerate(list):
#     if v == max(list):
#         print(f'{i}...0', end='')

# for i, v in enumerate(list):
#     if v == min(list):
#         print(f'{i}...0', end='')
