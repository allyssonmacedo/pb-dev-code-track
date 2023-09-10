# crie um programa onde o usuário digita uma expressão qualquer que use parenteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.


expression = input('Digite a expressão com os parenteses: ')
list = list()

for sym in expression:
    if sym == '(':
        list.append('(')
    elif sym == ')':
        if len(list) > 0:
            list.pop()
        else:
            list.append(')')
            break

if len(list) == 0:
    print('Sua expressão está válida')

else:
    print('Sua expressão está errada')