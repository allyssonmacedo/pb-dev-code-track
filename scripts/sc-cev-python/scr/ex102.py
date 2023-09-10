## Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show = False):
    """
    -> Calcula o fatorial de um número
    :param n: o número a ser calculado
    :param show: (opcional) Mostrar ou não a conta
    :return: O valor do Fatorial de um número n
    """
    fact = 1
    for n in range(num, 0, -1):
        if show:
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end ='')    
        fact *= n
    return fact

print(fatorial(5, True))
print(fatorial(5))
