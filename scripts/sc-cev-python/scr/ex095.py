# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = []

while True:
    nome_jogador = str(input('Digite o nome do jogador: '))
    qtd_partidas = int(input(f'Digite o número de partidas que o {nome_jogador} jogou: '))
    gols = []
    counter = 1

    for partida in range(qtd_partidas):
        gols_partidas = int(input(f'Digite o número de gols na {counter}º partida: '))
        gols.append(gols_partidas)
        counter += 1

    dic_matches = {
        'jogador': nome_jogador,
        'qtd_partidas': qtd_partidas,
        'gols_na_partida': gols,
        'total_gols': sum(gols)
        }
    
    time.append(dic_matches)

    while True:
        resp = str(input('Quer continuar ? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-' * 40)
print('cod ', end = '')
for i in dic_matches.keys():
    print(f'{i:<15}', end = '')

print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<15} ', end= '')
    print()

print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Nao existe jogador com o código {busca} ')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["jogador"]}: ')
        for i, g in enumerate(time[busca]["gols_na_partida"]):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print(' << Volte Sempre >>')

# print(f'==> O jogador {dic_matches["jogador"]} fez {dic_matches["qtd_partidas"]} partidas e {dic_matches["total_gols"]} gols')

# for i, v in enumerate(dic_matches['gols_na_partida']):
#     print(f'Na partida {i}, fez {v} gols ')
# print(dic_matches)