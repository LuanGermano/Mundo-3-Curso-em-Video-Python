# Faça um programa que tenha uma lista chamada NUMEROS e duas funções
#Chamada SORTEIO e SOMAPAR. a primeira vai sortear 5 numeros e botar numa lista
# o segundo vai mostrar a soma dos valores pares da lista.
from random import randint
numeros= list()


def sorteio():
    for n in range(0, 5):
        numeros.append(randint(0, 10))
    print('A Lista é:', end=' ')
    print(*numeros)


def somapar():
    s = 0
    for v in numeros:
        if v % 2 == 0:
            s += v
    print(f'A soma de seus valores é: {s}')


sorteio()
somapar()


