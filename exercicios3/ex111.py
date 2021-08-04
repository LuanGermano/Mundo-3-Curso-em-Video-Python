#Crie um pacote chamado UTILIDADES CEV que tenha dois modulos internos chamado MOEDA e dado.
# transfira todas as fnções utilizados nos desafios para o primeiro
from UtilidadesCeV.dados import leiaDinheiro
from UtilidadesCeV.moedas import moedas


p = leiaDinheiro('Digite um valor: ')
d = int(input('Adicione o valor de desconto: '))
a = int(input('Adicione o valor de acrescimo: '))
moedas.resumo(p, a, d)