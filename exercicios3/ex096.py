# Faça um programa que tenha uma FUNÇÃO chamada AREA, que recebea as dimensões de um terreno retangular
# mostre a area do terreno
def area(a, b):
    print(f'A area de um terreno {a}mX{b}m tem:', end=' ')
    m = a * b
    print(f'{m}m²')


l1 = float(input('Largura (m): '))
l2 = float(input('Comprimento (m): '))
area(l1, l2)
