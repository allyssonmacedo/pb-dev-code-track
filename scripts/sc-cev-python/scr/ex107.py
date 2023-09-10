# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().

# Faça também um programa que importe esse módulo e use algumas dessas funções.

import pacotes.moeda as moeda

x = moeda.aumentar(10,100)

y = moeda.diminuir(10,2)

w = moeda.dobro(10)

z = moeda.metade(5)


print(x,y,w,z)