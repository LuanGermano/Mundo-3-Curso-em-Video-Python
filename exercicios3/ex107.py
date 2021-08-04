# Crie um modulo chamado Moeda.py que tenha as funções incorporadas
''' Aumentar(). diminuir(), dobro() e metade()'''
# Faça tambem um programa que importe esse modulo e use algumas dasessas funções
from UtilidadesCeV.moedas import moedas

p = float(input('Digite um Preço:R$ '))
d = int(input('Adicione o valor de desconto: '))
a = int(input('Adicione o valor de acrescimo: '))
print(f'A metade de {p} é {moedas.metade(p)}')
print(f'O dobro de {p} é {moedas.dobro(p)}')
print(f'Desconto de {d}% do valor do produto é {moedas.diminuir(p, d)} ')
print(f'Aumento de {a}% do valor do Produto é {moedas.aumentar(p, a)}')
