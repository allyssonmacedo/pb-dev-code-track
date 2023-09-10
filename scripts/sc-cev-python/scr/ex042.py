#Refaça o desafio 035 dos triângulos, acrescetando o recurso de mostrar que tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isósceles: dois lados iguais
#Escaleno : todos os lados diferentes


a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um triângulo')
    if a != b and b != c and a != c:
        print('O triângulo é escaleno')
    elif a == b == c:
        print('O triângulo é equilátero')
    else:
        print('O triângulo é isósceles')

else:
    print('Os segmentos acima não formam um triângulo')

