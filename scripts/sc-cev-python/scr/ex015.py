d = int(input('Por QUantos dias o carro foi alugado? '))
km = float(input('Quantos Km o carro rodou ? '))
f = float((60 * d) + (0.15 * km))

print('Você irá pagar R$ {:.2f}'.format(f))