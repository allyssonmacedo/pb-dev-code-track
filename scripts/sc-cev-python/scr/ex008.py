#Escreva um programa que leia um valor em metros e o exiba 
#convertido em centímetros e milimetros

v = float(input('Digite o valor em metros: '))
print('Pronto!, o valor em metros é de {} e em centímetros: {:.0f} e em milímetros {:.0f}!'.format(v, v*100, v*1000)) 