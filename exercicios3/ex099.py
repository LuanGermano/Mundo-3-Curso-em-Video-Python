# faça um programa que tenha uma função chamda MAIOR que receba varios parametros
# Seu programa tem q analisar todos os valores e dizer qual deles é o maior.

from random import randint  # Trazendo o aleatorizador

lista = list()  # Lista pra colocar os numeros
n = randint(4, 11)  # Definindo no inicio do programa o valor q sera o tamanho da minha lista.


def linha():  # Função de linha
    print('-=' * 14)


def rand():  # Função q vai adicionar os valores aleatorios dentro da lista com limite estabelecido por n
    for c in range(0, n):
        r = randint(0, 100)
        lista.append(r)


def maior(num):  # Função onde procura o maior valor dentro da minha lista estabelecida
    mai = 0
    print(f'Possui {len(num)} valores \nA lista de numeros é:', end=' ')
    for v in num:  # Verificação de maior valor dentre todos os da lista.
        print(v, end=' ')
        if mai < v:  # checagem de verificação
            mai = v  # atribuindo o maior valor
    print()
    print(f'O maior numero da lista é {mai}')
    linha()

linha()
for c in range(0, n - 3):  # pra fazer o programa gerar mais de 1 resultado(as vezes
    rand()
    maior(lista)
    lista.clear()
