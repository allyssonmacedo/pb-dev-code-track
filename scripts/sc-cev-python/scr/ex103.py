# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.

# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome='<Desconhecido>', gols=0):
    """Retorna o nome do jogador e quantos gols ele marcou

    Args:
        nome (str, optional): Nome do jogador. Defaults to '<Desconhecido>'.
        gols (int, optional): Quantos gols ele marcou. Defaults to 0.
    """
    print(f'O jogador {nome} marcou {gols}')

nome = str(input('Digite o nome do jogador: '))
gols = str(input('Quantos gols o jogador fez? '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gols = gols)
else:
    ficha(nome, gols)
