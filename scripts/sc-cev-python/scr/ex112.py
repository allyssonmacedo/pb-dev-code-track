# Dentro do pacote utilidades CeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from pacotes import dado
from pacotes import moeda

p = dado.leiaDinheiro('Digite o preço: ')
moeda.resumo(p)