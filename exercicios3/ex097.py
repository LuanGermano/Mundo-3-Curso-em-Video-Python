# Faça um programa que tenha uma FUNÇÂO chamada ESCREVA(), que receba o texto qualqer
# como parametro e mostre uma mensagem com tamanho adaptavel.
def escreva(txt):
    print('~' * (len(txt) + 2))
    print(f' {txt}')
    print('-' * (len(txt) + 2))


escreva(str(input('Digite um texto: ')).strip())
