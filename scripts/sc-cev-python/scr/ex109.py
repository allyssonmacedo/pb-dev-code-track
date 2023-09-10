# modifique as funções que foram criadas no desafio 107, para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

import pacotes.moeda as moeda

x = moeda.aumentar(10,100, True)

y = moeda.diminuir(10,2, True)

w = moeda.dobro(10, True)

z = moeda.metade(5, True)


print(x,y,w,z)