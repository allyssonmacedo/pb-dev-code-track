#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Gurde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random, time
from operator import itemgetter

dic = {
    'player1': random.randint(1,6),
    'player2': random.randint(1,6),
    'player3': random.randint(1,6),
    'player4': random.randint(1,6)
}

ranking = []

for k, v in dic.items():
    print(f' {k} jogou o valor {v}')
    time.sleep(1)
ranking = sorted(dic.items(), key = itemgetter(1), reverse=True)

print('-=' * 30)
print('RANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    time.sleep(1)
