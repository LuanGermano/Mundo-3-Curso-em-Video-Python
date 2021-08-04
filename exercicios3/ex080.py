# Crie um programa onde o usuario possa digitar Cinco valores se bota na lista.
# Ja na posição correta de inserção (sem usar o SORT). No final mostre a lista ordenada na tela
# Tem q ir colocando na posição crescente respeitando os numeros ja colocados, parece complicado # FOI COMPLICADO
lista = []
for c in range(0, 5):
    num = int(input('Digite outro valor: '))
    lista.append(num)
print(lista)
for pos, valor in enumerate(lista):
    if lista[0] > lista[pos]:
        lista.pop(pos), lista.insert(0, valor)
    elif lista[1] > lista[pos]:
        lista.pop(pos), lista.insert(1, valor)
    elif lista[2] > lista[pos]:
        lista.pop(pos), lista.insert(2, valor)
    elif lista[3] > lista[pos]:
        lista.pop(pos), lista.insert(3, valor)
    elif lista[4] > lista[pos]:
        lista.pop(pos), lista.insert(4, valor)
print(lista)

# CASO N DE CERTO O CODIGO ACIMA, TENTAR CO ENUMERATE
# OQ EU QUERO NESSE CARALHO
# COMPARE O PRIMEIRO VALOR DA LISTA COM TODOS OS NUMEROS
# se o primeiro valor for menor que o valor X, ele vai avançar pra tras
# o valor X virara o primeiro valor e sumir da posição Y
