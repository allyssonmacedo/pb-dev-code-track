#Escreva um programa para aprovar um empréstimo bancário para comprar uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos le vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado


v_casa = float(input('Digite o valor da casa (em R$): '))
v_sal = float(input('Digite o valor do seu salário (em R$):  '))
tempo = float(input('Em quanto tempo você pretende quitar o imóvel? (em meses) '))
valor_pagar = v_casa / tempo

if valor_pagar <= 0.3 * v_sal:
    print(f'\033[0:33m Parabéns \033[m, seu imóvel foi aprovado!. Você deverá pagar R$ {valor_pagar:.2f} durante {tempo:.2f} meses ({(tempo / 12):.2f}) anos')
else:
    print(f'O valor da prestação (R$ {valor_pagar:.2f}) excedeu o limite permitido e por esta razão, \033[0:33m seu financiamento não foi aprovado. \033[m')

