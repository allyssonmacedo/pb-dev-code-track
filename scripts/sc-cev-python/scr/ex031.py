#Desenvolva um programa que pergunte a distância de uma viagem em Km
#Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200 km
# e R$ 0,45 para viagens mais longas:


try: 
    dist = float(input('Digite a distância da sua viagem: '))
    if dist <= 200:
        print(f'O preço da passagem é de {0.5 * dist}')
    else: 
        print(f'O preço da passagem é de {0.45 * dist}')
except:
    print('você digitou algo errado, tente novamente')