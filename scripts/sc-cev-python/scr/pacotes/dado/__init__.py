def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha():
            print('Erro. Por favor, digite um número')
        else:
            válido = True
            return float(entrada)