# Crie um programa onde o usuario possa digitar sete valores numericos e cadastre os em uma lista unica,
# Que separe os Pares dos IMpares. No final mostre os valores pares e impares em ordem crescente.
# imagina q seja assim?
# valores = [['''pares'''], ['''Impares''']]
dados = [[], []]
valores = list()
for v in range(0, 7):
    val = (int(input('Digite um valor: ')))
    if val % 2 == 0:
        valores.append(val)
        dados[0].append(valores[:])
        valores.clear()
    else:
        valores.append(val)
        dados[1].append(valores[:])
        valores.clear()
dados[0].sort()
dados[1].sort()
print(f'Os valores Pares são: ', end='')
print(*dados[0], sep=',')
print(f'Os valores impares são: ', end='')
print(*dados[1], sep=',')
