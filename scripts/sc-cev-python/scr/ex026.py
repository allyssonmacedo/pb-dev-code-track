#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = str(input('Digite a frase: ')).strip()
qnt_A = frase.count('A')
print(qnt_A)

primeiro = frase.find('A')
ultimo = frase.rfind('A')

print(primeiro, ultimo)