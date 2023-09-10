#Crie um programa que leia 2 notas de um aluno e calcule a sua média, mostrando se media abaixo de 5 reprovado, 5 a 6.9 recuperação, superior a 7 aprovado

n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média foi {media}. Você está reprovado')
elif media >= 5 and media < 7:
    print(f'Sua média foi {media}. Você está de recuperação')
else:
    print(f'Sua média foi {media}. Você está aprovado')