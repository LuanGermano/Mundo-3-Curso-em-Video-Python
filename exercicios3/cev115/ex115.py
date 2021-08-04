# Crie um pequeno sistema modularizado que permita cadastrar pessoas
# pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções, cadastrar uma nova pessoa e listar todas as cadastradas
# OFICIAL
from modulo115 import cadastro, linha, menu
from cor import cores
linha()
print(f'\033[34m{"Menu Principal":^40}\033[m')

while True:
    alternativas = menu()

    if alternativas == 1:
        linha()
        print(f'{cores["cya"]}{"Opção 1":^40}{cores["cle"]}')
        linha()
        pessoas = open('cadastro.txt', "r")
        for linhas in pessoas:
            linhas = linhas.rstrip()
            print(linhas)
        pessoas.close()

    elif alternativas == 2:
        linha()
        print(f'{cores["cya"]}{"Opção 2":^40}{cores["cle"]}')
        linha()
        pessoa = cadastro()

    else:
        linha()
        print(f'{cores["cya"]}{"FECHANDO O PROGRAMA":^40}{cores["cle"]}')
        linha()
        break
