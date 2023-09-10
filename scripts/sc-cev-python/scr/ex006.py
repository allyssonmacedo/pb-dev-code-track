#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = float(input('digite um número inteiro: '))
print('O seu número é {}, o dobro do seu número é {},\n e o triplo é {}.'.format(n, 2*n, 3*n), end = ' >>> ')
print('A raiz quadrada do número é {:.2f}'.format(n**(1/2)))