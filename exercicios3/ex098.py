# Faça um programa que tenha uma função chamada contador()
# Recebera tres parametros, Inicio, FIm e passo e realize a contagem
# IGual um for??
# Seu programa deve realizar TRES CONTAGENS atraves da função criada:
'''
A) de 1 ate 10, de 1 em 1
B)de 10 ate 0, de 2 em 2
C)uma contagem personalizada.
'''
from time import sleep


def linha():
    print('-=' * 20)


def contador(i, f, p):
    linha()
    print(f'A lista de valores de {i} ate {f} com passo {p} sera: ')
    if p == 0:
        p = 1
    if i > f:
        if p > 0:
            p = -p
        while i >= f:
            print(i, end=' ')
            i += p
            sleep(0.25)
    elif i < f:
        while i <= f:
            print(i, end=' ')
            i += p
            sleep(0.25)
    print('Fim')


contador(1, 10, 1)
contador(10, 0, 2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

