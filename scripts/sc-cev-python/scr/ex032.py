#Verificar se o ano é bissexto

try:
    ano = int(input('Digite um ano qualquer: '))
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano é bissexto')
    else: 
        print('O ano não é bissexto')
except:
    print('Você digitou algo de errado, tente novamente')
