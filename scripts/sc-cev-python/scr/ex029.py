#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80 km/h mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$ 7,00 por cada Km acima do limite

while True:
    try: 
        veloc = float(input('Qual a velocidade em Km/h? '))
        if veloc <= 80:
            print('Continue assim, você está na faixa permitida.')
        else:
            valor_multa = (veloc - 80) * 7
            print(f'Você ulrapassou a velocidade e receberá uma multa de R$ {valor_multa}')
        print('Fim do programa')
        break
    except: 
        print('Você digitou valores inválidos, tente novamente')

