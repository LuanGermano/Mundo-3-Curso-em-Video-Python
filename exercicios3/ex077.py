#Crie um programa que tenha uma tupla com VARIAS PALAVRAS.
# Depois disso vc deve mostrar, para cada palavra, quais sao suas vogais.
palavras = ('Olho', 'Cabeça', 'ombro', 'Joelho', 'pe', 'boca', 'nariz', 'mao', 'cotovelo', 'pescoço')
for p in palavras:
    print('\n', '-=-' * 15)
    print(f'A palavra {str(p).title()} tem as seguintes vogais:', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')

""" if 'a' in p:  # preciso pegar o P e descobrir quais vogais tem nele
    print('A', end='')
if 'e' in p:
    print('E', end='')
if 'i' in p:
    print('I', end='')
if 'o' in p:
    print('O', end='')
if 'u' in p:
    print('U', end='')"""

