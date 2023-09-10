# crie um programa onde o usuário possa digitar cinco valores numéricos  e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela

list = []
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > list[-1]:
        list.append(n)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Os valores digitados em ordem foi {list}')