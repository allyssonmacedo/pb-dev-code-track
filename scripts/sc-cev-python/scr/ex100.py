## Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar(). A primeira função vai sortear 5 números e colocá-las dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

valores = list()

def sorteio():
    for rand in range(0,5):
        rand = randint(1,10)
        valores.append(rand)
    print(f' Os valores sorteados foram {valores}')

def somaPar(list):
    list_par = []
    for item in list:
        if item % 2 == 0:
            list_par.append(item)
    print(f' A soma dos valores pares são {sum(list_par)}')


sorteio()
somaPar(valores)    