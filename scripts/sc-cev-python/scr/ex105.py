# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#-Quantidade de notas
#-A maior nota
#-A menor nota
#-A média da turma
#-A situação (opcional)
#Adicione também as docstrings da função


def notas(*notas: float, situação = False):
    """Fornece estatística sobre um conjunto de notas informadas

    Args:
        notas (list): lista com notas adicionadas
        situação (bool, opcional): Se deve mostrar ou não a situação da turma.
    Returns:
        dicionario (dic): Dicionário com as informações sobre quantidade de notas digitadas, máxima nota, média das notas e situação (se aplicável)
    """

    len_notas = len(notas)
    max_notas = max(notas)
    med_notas = sum(notas) / len_notas

    dic = {
    'total_notas': len_notas,
    'max_nota': max_notas,
    'med_notas': med_notas,
    }

    if situação == True:
        if med_notas >= 8: 
            dic['situação'] = 'Boa'
        elif med_notas > 6:
            dic['situação'] = 'Regular'
        else:
            dic['situação'] = 'Ruim'

    return dic
    
print(notas(10,8,7,8,9))





#### Código de algum comentário do Youtube:
# def notas(*n, sit=False, tab=False):
#     """
#     -> Função para analisar funções e situações de vários alunos.
#     :param n: uma ou mais notas dos alunos (aceita várias).
#     :param sit: opcional, indica se deve ou não adicionar a situação da turma.
#     :param tab: opcional, indica se deve ou não mostrar os dados em forma de tabela.
#     :return: dicionário e/ou tabela com os dados solicitados.
#     """
#     dados = {}
#     total = maior = menor = soma = 0
#     s = ''
#     for i in n:# laço para obter: total, maior, menor e soma
#         soma += i
#         total += 1
#         if i == n[0]:
#             maior = i
#             menor = i
#         else:
#             if i > maior:
#                 maior = i
#             if i < menor:
#                 menor = i
#     media = soma / total# cálculo da média das notas
#     if media < 5:# classificação da situação de acordo com a média de notas.
#         s = 'RUIM'
#     if 5 <= media < 7:
#         s = 'RAZOÁVEL'
#     if media > 7:
#         s = 'BOA'
#     dados['total'] = total
#     dados['maior'] = maior
#     dados['menor'] = menor
#     dados['média'] = media
#     if sit == True:# opção caso desejar mostrar a situação da sala, de acordo com a média.
#         dados['situação'] = s
#     if tab == True:# opção caso desejar mostrar os dados em forma de tabela.
#         if sit == True:
#             print()
#             print('=' * 50)
#             print(f'\033[1;34;43m{"ALUNOS DA SALA (NOTAS)":^50}\033[m')
#             print('=' * 50)
#             print(f'{"Total":<10}{"Maior":<10}{"Menor":<10}{"Média":<10}{"Situação":<12}')
#             print('-' * 50)
#             print(f'{dados["total"]:<10}{dados["maior"]:<10}{dados["menor"]:<10}{dados["média"]:<10.3f}{dados["situação"]:<12}')
#             print()
#         else:
#             print()
#             print('=' * 37)
#             print(f'\033[1;34;43m{"ALUNOS DA SALA (NOTAS)":^37}\033[m')
#             print('=' * 37)
#             print(f'{"Total":<10}{"Maior":<10}{"Menor":<10}{"Média":<10}')
#             print('-' * 37)
#             print(f'{dados["total"]:<10}{dados["maior"]:<10}{dados["menor"]:<10}{dados["média"]:<10.3f}')
#             print()

#     return dados



# # Programa Principal
# num = []
# while True:
#     g = float(input('Digite a nota: '))
#     num.append(g)
#     r = str(input('Deseja continuar?[S/N]: ')).strip().upper()[0]
#     if r == 'N':
#         break
# print('-' * 40)
# situation = str(input('Deseja mostrar a situação?[S/N]: ')).strip().upper()[0]
# tabela = str(input('Deseja mostrar em tabela?[S/N]: ')).strip().upper()[0]
# if situation == 'S':
#     if tabela == 'S':
#         resp = notas(*num, sit=True, tab=True)
#     else:
#         resp = notas(*num, sit=True)
# else:
#     if tabela == 'S':
#         resp = notas(*num, tab=True)
#     else:
#         resp = notas(*num)
# print()
# print(resp)