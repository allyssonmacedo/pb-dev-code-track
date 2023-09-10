# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

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

print(f'==> O jogador {dic_matches["jogador"]} fez {dic_matches["qtd_partidas"]} partidas e {dic_matches["total_gols"]} gols')

for i, v in enumerate(dic_matches['gols_na_partida']):
    print(f'Na partida {i}, fez {v} gols ')
print(dic_matches)

# counter2 = 1
# for gol_part in enumerate(gols):
#     print(f'Na partida {counter2} o {dic_matches["jogador"]} fez {gol_part[1]}')
#     counter2 += 1