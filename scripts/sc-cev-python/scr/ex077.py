# crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as vogais.

listagem = (
    'lapis',
    'caneta',
    'pincel',
    'caderno',
    'borracha',
    'adesivos',
)

for palavra in listagem:
    print(f'\n Na palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
