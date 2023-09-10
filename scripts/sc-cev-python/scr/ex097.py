## Faça um programa que tenha uma função chamada escreva() que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva('Olá, mundo!')
#-----------
#Olá, mundo!
#-----------

def escreva(txt):
    len_txt = len(txt) + 4 #para passar um pouco
    print('-' * len_txt)   
    print(f'  {txt}')  #para centralizar (2 espaços na esquerda e 2 na direita)
    print('-' * len_txt)

escreva('Olaaa, mundo!')
