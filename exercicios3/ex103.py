# Faça um programa que tenha uma função chamada FICHA(), que receba dois parametros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado n tenha sido informado
def ficha(j, g):
    """
    Programa que mostra um jogador e os seus gols num campeonato
    :param j: Nome do jogador
    :param g: Gols feitos
    :return: não possui
    """
    if j == '':
        j = '<Indefinido>'
    print(f'O jogador {j} fez {g} gol(s) no campeonato')


nome = str(input('Nome do Jogador: ')).strip()
gols = str(input('Numero de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
ficha(nome, gols)
