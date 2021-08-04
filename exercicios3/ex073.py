# Crie uma tupla preencida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol,
# na ordem de colocação. Depois Mostre:
'''
A) Apenas os primeiros 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela
C) Uma lista com os nomes dos times em Ordem alfabetica
D) Em que posição na tabela esta o time CHAPECOENSE'''

tabela = ('Bragantino', 'Athletico-PR', 'Palmeiras', 'Atletico-MG', 'Fortaleza', 'Bahia', 'Atletico-GO', 'Ceara',
          'Fluminense', 'Flamengo', 'Santos', 'Juventude', 'Corinthians', 'Internacional', 'America-MG', 'Sport',
          'São Paulo', 'Cuiaba', 'Chapecoense', 'Gremio')
print('-=-'*14)
print(f'A) Os 5 primeiros colocados são {tabela[:5]}')
print('-=-'*14)
print(f'B) Os ultimos 4 colocados são {tabela[-4:]}')
print('-=-'*14)
print(f'C) Em ordem alfabetica os times são {sorted(tabela)}')
print('-=-'*14)
print(f'D) A Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição ')
print('-=-'*14)
