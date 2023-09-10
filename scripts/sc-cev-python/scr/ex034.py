#Escreva um programa que pergunte o salário de um funcionário e calcule 
#o valor do seu aumento
#Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
#Para inferiores ou iguais, o aumento é de 15%


try:
    sal = float(input('Digite o valor do seu salario: '))
    if sal > 1250:
        print(f'O seu salário será de {sal * 1.1}')
    else:
        print(f'O seu salário será de {sal * 1.15}')
except:
    pass