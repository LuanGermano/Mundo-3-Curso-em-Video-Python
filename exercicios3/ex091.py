# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios.
# Guarde esses resultados em um dicionario. no final, Coloque em ordem, vencedor tirou maior.
# resultado de cada jogador e separado a posição de cada
from random import randint
from time import sleep
from operator import itemgetter  # uma sinxtaxe pra auxiliar na organização

resultado = {}
resultado['jogador 1'] = randint(1, 6)  # Randomização pra lista, fiz fora dela mas podia ser feita já dentro
resultado['jogador 2'] = randint(1, 6)
resultado['jogador 3'] = randint(1, 6)
resultado['jogador 4'] = randint(1, 6)
ordem = {}  # Dicionario auxliar onde ficam os numeros ordenados, mas que vai se transformar em lista ao usar itemgetter
for k, v in resultado.items():  # Para cada jogador e resultado nos items do dicionario
    sleep(0.25)
    print(f'O {k} tirou {v}')
    sleep(0.5)
print(f'as colocações ficaram:')
ordem = sorted(resultado.items(), key=itemgetter(1), reverse=True) '''Foi adicionado em ordem os numeros presentes em resultados
utilizando do itemgetter pra definir quais serão os valores base pra ordenação e no final a lista é revertida'''
for i, v in enumerate(ordem):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.7)