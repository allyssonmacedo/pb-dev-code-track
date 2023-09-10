#faça um programa que leia 3 números e diga qual o maior e menor:

from ast import Return


n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))

#Tratando os maiores números:
if n1 != n2 and n1 != n3 and n2 != n3:
    if n1 > n2 and n1 > n3: 
        print('O primeiro número é o maior número')
    elif n2 > n1 and n2 > n3:
        print('O segundo número é o maior deles')
    elif n3 > n1 and n3 > n2:
        print('O terceiro número é o maior deles')

elif n2 == n3 and n1 > n2:
    print('O primeiro número é o maior deles')
elif n3 == n1 and n2 > n1:
    print('O segundo número é o maior deles')
elif n1 == n2 and n3 > n1:
    print('O terceiro número é o maior deles')
else:
    print('Há mais de um maior possível para esta resposta')


#Tratando os menores números:
if n1 != n2 and n1 != n3 and n2 != n3:
    if n1 < n2 and n1 < n3: 
        print('O primeiro número é o menor número')
    elif n2 < n1 and n2 < n3:
        print('O segundo número é o menor deles')
    elif n3 < n1 and n3 < n2:
        print('O terceiro número é o menor deles')

elif n2 == n3 and n1 < n2:
    print('O primeiro número é o menor deles')
elif n3 == n1 and n2 < n1:
    print('O segundo número é o menor deles')
elif n1 == n2 and n3 < n1:
    print('O terceiro número é o menor deles')
else:
    print('Há mais de um maior possível para esta resposta')