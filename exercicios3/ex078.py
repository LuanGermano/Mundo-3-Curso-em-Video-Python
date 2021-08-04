lista = list()
maxcont = mincont = 1

for c in range(0, 5):
    val = int(input(f'Digite um valor para posição {c}: '))
    lista.append(val)
print(*lista, sep=', ')
maior = max(lista)
posmaior = lista.index(max(lista))
menor = min(lista)
posmenor = lista.index(min(lista))

print(f'O maior valor da Lista é o {maior} na posição {posmaior} ')
print(f'O menor valor da lista é o {menor} na posição {posmenor}')
lista.sort()
if lista[0] == lista[1]:
    mincont += 1
    if lista[1] == lista[2]:
        mincont += 1
if lista[-1] == lista[-2]:
    maxcont += 1
    if lista[-2] == lista[-3]:
        maxcont += 1
print(f'O Maior valor se repete {maxcont}x ')
print(f'O menor valor se repete {mincont}x ')