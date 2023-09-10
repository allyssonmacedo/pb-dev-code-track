## Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função input() do Python. Só que fazendo a validação para aceitar apenas um valor númerico. 

#Ex.: 
#n = leiaint('Digite um n')

def leiaint(txt: str):
    """Lê um número inteiro

    Args:
        txt (str): mensagem a ser convertida
    """

    ok = False
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido. \033[m')
        if ok:
            break
    return valor

n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')

    