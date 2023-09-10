## pacote

def aumentar(x, y, formatar_moeda=False):
    res = x + (x * y)/100 
    return res if moeda is False else moeda(res)
    
def diminuir(x:float, y:float, formatar_moeda=False):
    res = x - (x * y)/100
    return res if moeda is False else moeda(res) 

def dobro(x: float, formatar_moeda = False):
    res = x * 2
    return res if moeda is False else moeda(res) 

def metade(x:float, formatar_moeda = False):
    res = x / 2
    return res if moeda is False else moeda(res) 
    
def moeda(valor, moeda_ = 'R$'):
    return f'{moeda_} {valor:.2f}'.replace('.', ',')

def resumo(valor):
    print('-' * 30)
    print(f'10 % de aumento sobre o valor de {moeda(valor)} é {(aumentar(valor, 10, True))}')
    print(f'17 % de redução sobre o valor de {moeda(valor)} é {(diminuir(valor, 17, True))}')
    print(f'O dobro do valor de {moeda(valor)} é {(dobro(valor, True))}')
    print(f'A metade do valor de {moeda(valor)} é {(metade(valor, True))}')