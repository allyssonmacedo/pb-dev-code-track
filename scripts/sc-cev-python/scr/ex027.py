#Faça um programa que leia o nome completo de uma pessoa, mostrando em 
#em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#primeiro = Ana
#Último = Souza


nome_completo = str(input('digite o seu nome: ')).strip()
nome_quebrado = nome_completo.split()
primeiro = nome_quebrado[0]
ultimo = nome_quebrado[-1]

print(primeiro, ultimo)