# Dentro do pacote UTILIDADESCEV que criamos no desafio 11, temos um modulo dado.
# crie a função chamada leiadinheiro() que seja capaz de funcionar como a função Input()

from UtilidadesCeV.dados import leiaDinheiro
from UtilidadesCeV.moedas import moedas


p = leiaDinheiro('Digite um valor: ')
d = int(input('Adicione o valor de desconto: '))
a = int(input('Adicione o valor de acrescimo: '))
moedas.resumo(p, a, d)
