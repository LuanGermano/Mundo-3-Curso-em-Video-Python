# adicione ao modulo __init__.py criado nos desafios anteriores uma função chamda Resumo()
# Que mosstra na tela algumas informações geradas pelas funções que já temos no modulo

from UtilidadesCeV.moedas import __init__

p = float(input('Digite um Preço:R$ '))
d = int(input('Adicione o valor de desconto: '))
a = int(input('Adicione o valor de acrescimo: '))
__init__.resumo(p, a, d)