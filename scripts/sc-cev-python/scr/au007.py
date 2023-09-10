nome = input('Qual o seu nome? ')
print('Prazer em te conhecer: {:>20}!'.format(nome))
print('Prazer em te conhecer: {:<20}!'.format(nome))
print('Segundo modo, {:^20}!'.format(nome))
print('Olha como fica agora, {:=^20}!'.format(nome))


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
d = n1 / n2
e = n1 ** n2
di = n1 // n2
r = n1 % n2
print('A soma é {}, a subtração é {}, a divisão é {:.3f}, \n a exponenciação é {}, a divisão inteira é {} \n e o resto da divisão é {}'.format(s, sub, d, e, di, r))
# Para quebrawr usa-se vírgula seguida de end=' '
# Ou então usa uma \n 
print('A soma é {}, a subtração é {}'.format(s, sub), end='  >>>  ')
print('A divisão é {} e potência é {}'.format(d, e)) 
