# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []
menu = 0

while True:
    while menu not in [1,2,3]:
        print('O que você deseja fazer? \n [1] adicionar alunos \n [2] ver notas \n [3] mostrar todas as notas')
        menu = int(input('Digite o número correspondente: '))

    if menu == 1:
        while True:
            nome = str(input('Digite o nome do aluno: '))
            nota1 = float(input('Digite a primeira nota: '))
            nota2 = float(input('Digite a segunda nota: '))
            media = (nota1 + nota2)/2
            alunos.append([nome, [nota1, nota2], media])
            print(f'Aluno {nome} adicionado com média {media}')
            new_aluno = str(input('Deseja adicionar um novo aluno? [S/N] '))
            if new_aluno in 'Nn':
                menu = 0
                break
    
    # Opção de fazer mostrando o índice dos alunos e depois mostrar o valor das notas.
    if menu == 2:
        nome_alunos = []
        print('Temos os alunos cadastrados abaixo: ')
        for id in range (len(alunos)):
            nome_alunos.append(alunos[id][0])
        print(nome_alunos)
        aluno_ver = str(input('Digite o nome do aluno que deseja visualizar as notas '))
        aluno_id = alunos.index(aluno_ver)
        try:
            print(f'As notas do {aluno_ver} são {alunos[aluno_id][1]} com média {alunos[aluno_id][2]}')
            menu = 0

        except Exception as e:
            pass

    if menu == 3:
        print(f'''
            aluno .......... nota1 .......... nota 2 .......... média ''')
        for aluno in alunos:
            print(f'''
            {aluno[0]} .......... {aluno[1][0]} .......... {aluno[1][1]} .......... {aluno[2]}
            ''')
        menu = 0
        
        
        

    