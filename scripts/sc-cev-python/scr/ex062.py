#Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos


primeiro_termo = int(input('Digite o primeiro termo: '))
razão = float(input('Digite a razão: '))
termo = 1
decimo_termo = primeiro_termo + (10-1) * razão
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while termo <= total:
        valor = primeiro_termo + (termo * razão)
        termo += 1
        print(f'{valor}', end = ' -> ')
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'A progressão possui {total} termos')

