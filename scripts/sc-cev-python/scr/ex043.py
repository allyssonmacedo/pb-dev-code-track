#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do peso
#Entre 18.5 a 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida


peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual sua altura em metros? '))
IMC = peso / (altura **2)


if IMC <= 18.5:
    print("Você está Abaixo do peso")
elif IMC <= 25:
    print("Você está no Peso ideal")
elif IMC <= 30:
    print("Você está no Sobrepeso")
elif IMC <= 40:
    print("Você está na Obesidade")
elif IMC > 40:
    print("Você está na Obesidade mórbida")
