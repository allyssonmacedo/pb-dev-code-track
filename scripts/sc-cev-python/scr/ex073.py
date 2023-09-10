# crie uma tupla preenchida com os 10 primeiros colocados da tabela do campeonato brasileiro de futebol na ordem de colocação. Depois mostre:
# a) apenas os 5 primeiros colocados
# b) Os últimos 4 colocados da tabela 
# c) Uma lista com os times em ordem alfabética
# d) Em que posição na tabela está o time de chapecoense


tabela = ('fla', 'flu', 'botafogo', 'vasco', 'corinthias', 'palmeiras', 'chapecoense', 'havai', 'salvador', 'inter')

a = tabela[:5]
b = tabela[-4:]
c = sorted(tabela)
d = tabela.index('chapecoense') + 1

print(f'''
os cinco primeiros são {a} 
os últimos quatro são {b}
em ordem alfabética é {c}
chapecoense está em {d}
''')