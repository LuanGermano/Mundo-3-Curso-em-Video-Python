jogadores = list()
jogador = dict()
gols = []
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip().title()  # adição de chave e valor pro dict
    jogador['partidas'] = int(input('Partidas jogadas: '))  # Adição de partidas jogadas para ser usada no FOR
    for cont in range(0, jogador['partidas']):  # For pra cada partida
        gol = int(input(f'Quantos gols foram marcados na partida {cont+1}: '))
        gols.append(gol)  # Todos os gols marcados numa lista separada pra eles
    jogador['gols'] = gols.copy()  # e copiados para dentro do dicionario
    jogador['Total de gols'] = sum(gols)
    gols.clear()  # e limpado a lista pra renovação
    jogadores.append(jogador.copy())  # e adicionado o dicionario pra lista principal.
    print('*=*' * 16)
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()  # condição de controle
    while continuar not in "SN":  # condição de controle
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    print('-*=*-' * 12)
    if continuar == 'N':  # condição de parada
        continuar = ''
        break

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<12}', end='')
print()
print('--' * 16)
for i, j in enumerate(jogadores):
    print(f'{i:>3} ', end='')
    for d in j.values():
         print(f'{str(d):<12}', end='')
    print()
print('*=*' * 16)

while True:
    parada = int(input('Qual jogador deseja ver? '))  # busca de jogador
    print('--' * 16)
    if parada == 999 or parada >= len(jogadores):  # condições de parada
        print('Programa Encerrado.')
        break
    print(f'O jogador {jogadores[parada]["nome"]} jogou {jogadores[parada]["partidas"]} partidas')  # nome do jogador e quantas partidas jogou
    for n, valor in enumerate(jogadores[parada]['gols']):  # para cada valor e sua contagem dentro da lista dentro do dicionariod e gols
        print(f'Na partida {n+1} foram marcados {valor} gols')  # contagem de partidas e gols marcados
    print(f'O total de gols foi: {jogador["Total de gols"]}')  # Soma de gols na lista do dicionario.
    print('*-=-*' * 12)
