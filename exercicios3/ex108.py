# adapte o codigo do desafio 107, criando uma função chamada moeda()
# que consiga mostrar os valores como um valor monetario formatado.
from UtilidadesCeV.moedas import __init__

p = float(input('Digite um Preço:R$ '))
d = int(input('Adicione o valor de desconto: '))
a = int(input('Adicione o valor de acrescimo: '))
print(f'A metade de {__init__.moeda(p)} é {__init__.moeda(__init__.metade(p))}')
print(f'O dobro de {__init__.moeda(p)} é {__init__.moeda(__init__.dobro(p))}')
print(f'Desconto de {d}% do valor do produto é {__init__.moeda(__init__.diminuir(p, d))} ')
print(f'Aumento de {a}% do valor do Produto é {__init__.moeda(__init__.aumentar(p, a))}')
