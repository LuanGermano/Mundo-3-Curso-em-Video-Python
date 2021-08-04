# Aprimore o 093 para que ele funcione com VARIOS JOGADORES, incluindo um sistema de visualização
# DETALHES DO APROVEITAMENTO de cada jogador.
jogadores = list()
jogador = dict()
gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador: '))  # adição de chave e valor pro dict
    jogador['partidas'] = int(input('Partidas jogadas: '))  # Adição de partidas jogadas para ser usada no FOR
    for cont in range(0, jogador['partidas']):  # For pra cada partida
        gol = int(input(f'Quantos gols foram marcados na partida {cont+1}: '))
        gols.append(gol)  # Todos os gols marcados numa lista separada pra eles
    jogador['gols'] = gols.copy()  # e copiados para dentro do dicionario
    gols.clear()  # e limpado a lista pra renovação
    jogadores.append(jogador.copy())  # e adicionado o dicionario pra lista principal.
    print('*=*' * 16)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()  # condição de controle
    while continuar not in "SN":  # condição de controle
        continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    print('-*=*-' * 12)
    if continuar == 'N':  # condição de parada
        break


for c, i in enumerate(jogadores):  # Para cada jogador e seu respectivo numero na lista
    print(f'O jogador {jogadores[c]["nome"]} jogou {jogadores[c]["partidas"]} partidas')  # nome do jogador e quantas partidas jogou
    for n, valor in enumerate(jogadores[c]['gols']):  # para cada valor e sua contagem dentro da lista dentro do dicionariod e gols
        print(f'Na partida {n+1} foram marcados {valor} gols')  # contagem de partidas e gols marcados
    print(f'O total de gols foi: {sum(jogadores[c]["gols"])}')  # Soma de gols na lista do dicionario.
    print('*-=-*' * 12)
