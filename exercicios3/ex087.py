# Aprimore o 087 mostrando
'''
A)A soma de todos os valores pores digitados
B)A soma dos valores da terceira coluna.
C)O maior valor da segunda linha.
'''
matriz = [[], [], []]
pares = 0
some = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: ")))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    some += matriz[l][2]
    print()
print('A) A soma de todos os valores Pares dará: ', end='')
print(pares)
print('B) A soma dos valores da terceira coluna é: ', end='')
print(some)
print('C) O maior valor da segunda linha é: ', end='')
print(max(matriz[1]))
