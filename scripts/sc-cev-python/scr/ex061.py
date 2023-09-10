#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Digite o primeiro termo: '))
razão = float(input('Digite a razão: '))
termo = 1
decimo_termo = primeiro_termo + (10-1) * razão

while termo <= 10:
    valor = primeiro_termo + (termo * razão)
    termo += 1
    print(f'{valor}', end = ' -> ')
print('Fim da operação')