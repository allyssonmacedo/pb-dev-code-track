## Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno

def calcula_area(largura, comprimento):
    área = largura * comprimento
    print(f'O terreno possui {largura}m x {comprimento}m = {área}m² ')


while True:
    largura = float(input('Digite a largura do terreno em m: '))
    comprimento = float(input('Digite o comprimento do terreno em m: '))
    calcula_area(largura, comprimento)    