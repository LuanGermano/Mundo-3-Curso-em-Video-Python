# Crie um programa que gerencie o aproveitamento de um Jogador de futebol.
# O programa vai ler o NOME DO JOGADOR e QUANTAS PARTIDAS JOGOU. Depois vai ler QUANTIA DE GOLS em cada partida.
# No final, tudo isso será guardado em um dicionario, incluindo o TOTAL DE GOLS feitos durante o campeonato.
jogador = dict()
gols = []
jogador['nome'] = str(input('Nome do jogador: ')).title().strip()  # adição de chave e valor pro dict
jogador['partidas'] = int(input('Partidas jogadas: '))  # Adição de partidas jogadas para ser usada no FOR
for cont in range(0, jogador['partidas']):  # For pra cada partida
    gol = int(input(f'Quantos gols foram marcados na partida {cont+1}: '))
    gols.append(gol)  # Todos os gols marcados numa lista separada pra eles
jogador['gols'] = gols  # E adicionada no dicionario
jogador['total de gols'] = sum(gols)
print('*=*' * 12)

print(jogador)
for k, v in jogador.items():  # Parametro pra imprimir as chaves e seus valores;
    if k == "gols":  # Impedir a impressão da biblioteca de gols.
        break
    print(f'{k}: {v}')
print('*=*' * 12)
for contador, valor in enumerate(gols):  # repetição pra impressão dos gols usando a lista separada de gols.
    print(f'Na partida {contador+1} foram marcados {valor} gols')
print(f'O total de gols foi: {jogador["total de gols"]}')
print('*=*' * 12)
