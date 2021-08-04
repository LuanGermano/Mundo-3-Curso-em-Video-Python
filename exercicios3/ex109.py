# modifique as funções que foram criadas no desafio 107. para que eals aceitem UM PARAMETROa mais
# informando se quer o valor retornado por elas vai ser ou não formatado pela função moeda()
from UtilidadesCeV.moedas import __init__

p = float(input('Digite um Preço:R$ '))
d = int(input('Adicione o valor de desconto: '))
a = int(input('Adicione o valor de acrescimo: '))
s = str(input('Deseja formatar seu programa?[S/N] ')).upper().strip()
if s[0] == 'S':
    s = True
else:
    s = False
print(f'A metade de {__init__.moeda(p)} é {__init__.metade(p, s)}')
print(f'O dobro de {__init__.moeda(p)} é {__init__.dobro(p, s)}')
print(f'Desconto de {d}% do valor do produto é {__init__.diminuir(p, d, s)} ')
print(f'Aumento de {a}% do valor do Produto é {__init__.aumentar(p, a, s)}')
