# Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre
'''A)Quantas Pessoas foram cadastradas
B)Uma listagem com as pessoas mais pesadas.
C)Uma Listagem com as pessoas mais leves'''
# pessoas = [[pessoa0, peso1], [pessoa0, peso1]]

dados = list()
pessoa_peso = list()
pesma = []
mapeso = mepeso = 0
pesme = []

while True:
    pessoa_peso.append(str(input('Nome: ')).upper())
    pessoa_peso.append(float(input('Peso: ')))

    dados.append(pessoa_peso[:])
    pessoa_peso.clear()
    conti = str(input('Deseja adicionar mais alguem?[S/N] ')).upper()
    while conti not in 'SN':
        conti = str(input('Deseja adicionar mais alguem?[S/N] ')).upper()
    if conti == 'N':
        break

for nome, peso in dados:
    if mepeso == 0:
        mepeso = peso
        pesme.append(nome)
    elif peso < mepeso:
        pesme.clear()
        pesme.append(nome)
        mepeso = peso
    elif peso == mepeso:
        pesme.append(nome)

    if peso > mapeso:
        pesma.clear()
        pesma.append(nome)
        mapeso = peso
    elif peso == mapeso:
        pesma.append(nome)

print(f'Foram cadastradas {len(dados)} pessoas') # resp A
print(f'As pessoas mais pesadas são:', end=' ')
print(*pesma, sep=' e ', end=' ')
print(f'pesando {mapeso:.2f}Kg ')
print(f'As pessoas mais leves são:', end=' ')
print(*pesme, sep=' e ', end=' ')
print(f'pesando {mepeso:.2f}Kg ')







