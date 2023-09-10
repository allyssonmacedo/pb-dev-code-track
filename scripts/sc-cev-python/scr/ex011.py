#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária ppara pintá-la, sabendo que
# Cada litro de tinta pinta uma area de 2m²

larg = float(input('Insira a largura da parede em metros: '))
alt = float(input('Insira a altura da parede: '))
a = larg * alt 
print('VocÊ precisará de {} litros de tinta, pois cada litro pinta {} m² de parede.'.format(a/2, 2))