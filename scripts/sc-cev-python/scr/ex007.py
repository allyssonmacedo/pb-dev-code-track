#Desenvolva um programa que leia as duas notas de um aluno, 
# calcule e mostre a sua média  

nome = str(input('Qual o seu nome ? '))
print('Olá, {}!, Seja bem-vindo a nossa sala virtual!'.format(nome))
p = str(input('Deseja saber o resultado das suas provas? Digite sim ou não '))
if p == 'sim':
    p1 = float(input('Digite a primeira nota: '))
    p2 = float(input('Digite a segunda nota: '))
    pm = float(p1 + p2) / 2 
    if pm >= 7:
        print('Parabéns, você passou! A sua média é {}!!'.format(pm)) 
    if pm < 7: 
        print('Lamentamos, você não obteve a média mínima de aprovação. Sua nota foi {}'.format(pm))
if p == 'não':
    print('OK! Volte quando estiver pronto!')
