#Crie um programa que vai gerar CINCO NUMEROS ALEATORIOS e colocar em uma tupla.
# Depois dissso, mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla
from random import randint
random = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for n in random:
    print(f'{n} ', end='')
print(f'\n{max(random)} ')
print(min(random))
