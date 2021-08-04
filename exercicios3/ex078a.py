# Faça um programa que leia 5 valores numericos e guarde-os em uma lista.
# No final, mostr qual foi o maior e o menor valor digitando e as suas respectivas posições.
# bota algo caso tenha repetição do maior e menor valor

lista = []
posma = []
posme = []
for c in range(0,5):
    lista.append(int(input('Digite um valor: ')))
print(*lista, sep=', ')
for pos, val in enumerate(lista):
    if val == max(lista):
        posma.append(pos)
    if val == min(lista):
        posme.append(pos)
print(f'O maior valor dentro da minha lista é o {max(lista)} nas posições:', end='')
print(*posma, sep=' e ')
print(f'O menor valor dentro da minha lista é o {min(lista)} nas posições:', end='')
print(*posme, sep=' e ')
