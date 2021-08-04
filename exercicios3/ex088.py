# Faça um programa que ajude um jogador da mega Sena a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 numeros
# entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
# SEM REPETIÇÃO
from random import randint
from time import sleep
jogos = []
sort = int(input('Quantos Jogos deseja jogar? '))
for sorteio in range(0, sort):
    for n in range(0, 6):
        num = randint(1, 60)
        if num in jogos:
            num = randint(1, 60)
        jogos.append(num)
    print(f'O jogo {sorteio+1} sorteado é: ', end='')
    jogos.sort()
    print(*jogos)
    sleep(0.8)
    jogos.clear()
