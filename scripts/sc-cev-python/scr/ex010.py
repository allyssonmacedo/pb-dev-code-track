#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólarews ela pode comprar

dinheiro = float(input('QUanto de dinheiro você tem?: '))
conhecer_dolar = str(input('Você sabe quanto está o dolar hoje? Digite Sim ou Não ')) 

if conhecer_dolar == 'Sim':
    valor_dolar = float(input('Digite quanto está a cotação do dolar hoje (em Reais):')) 
    dolar = print('Você poderá comprar {:.4f} doláres com {} nesta cotação ({})'. format(dinheiro/valor_dolar, dinheiro, valor_dolar))
if conhecer_dolar == 'Não':
    dolar = print('VocÊ poderá comprar {:.4f} doláres com {} na cotação de hoje ({})!'.format(dinheiro/5.6, dinheiro, 5.6)) 
    
    