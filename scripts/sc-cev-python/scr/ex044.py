#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#A vista dinheiro: 10% de desconto ; à vista no cartão: 5% de desconto ; em até 2x no cartão: preço normal ; 3x ou mais no cartão : 20% de juros

print('Lojas Python')
preco = float(input('Digite o preço do produto: '))
print(
"""[1] À vista/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão"""
)

metodo = int(input('Digite o método de pagamento: '))

if metodo == 1:
    print(f'preço a ser pago é de R$ {0.9 * preco}')
if metodo == 2:
    print(f'preço a ser pago é de R$ {0.95 * preco}')
if metodo == 3:
    print(f'preço a ser pago é de {1.0 * preco}')
if metodo == 4:
    totalparc = int(input('Quantas parcelas? '))
    total = (1.2 * preco)
    print(f'preço a ser pago é de {1.2 * preco}')
else: 
    print("Favor, tente novamente")