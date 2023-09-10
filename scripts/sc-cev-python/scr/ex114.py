#Crie um código em Python que teste se o site Pudim está acessivel pelo computador usado.

import requests
import urllib

try:
    site = urllib.request.urlopen('https://www.google.com')
except urllib.error.URLError:
    print('O site Pudim não está acessível no momento')
else:
    print('Consegui acessar o site Pudim com sucesso')
    #print(site.read())