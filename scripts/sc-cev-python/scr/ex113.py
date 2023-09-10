# Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade

import ex104

while True:
    try:
        ex104
        break

    except:
        print("Digite um número válido")


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        
        except(ValueError, TypeError):
            print('\033[31mErro!, por favor, digite um número real válido. \033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[031mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n
        
n2 = leiaFloat('Digite um número real: ')
print(f'O valor real foi {n2}')

        