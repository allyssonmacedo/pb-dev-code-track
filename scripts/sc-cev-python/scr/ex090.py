# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

nome = str(input('Digite o nome do aluno: '))
avg_note = float(input('Digite a média do aluno: '))
if avg_note >= 7:
    status_approval = 'Aprovado'
else:
    status_approval = 'Reprovado'

aluno_dict = {
    'nome_aluno': nome,
    'média_notas': avg_note,
    'situação': status_approval}

print(f"Você digitou o(a) aluno(a) com o nome de {aluno_dict['nome_aluno']}, cuja média foi de {aluno_dict['média_notas']}.  A situação do aluno está {aluno_dict['situação']}")
