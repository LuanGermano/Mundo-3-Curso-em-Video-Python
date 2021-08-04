# Crie um programa que crie uma matriz de dimensão 3x3 e preenchida pelo teclado.
# No final mostre a Matriz na Tela com a formatação correta.
matriz_0_2 = []
matriz_1_2 = []
matriz_2_2 = []
nummatriz = []
for c in range(0, 3):
    nummatriz.append(int(input('Digite um Numero: ')))
    matriz_0_2.append(nummatriz[:])
    nummatriz.clear()
for c in range(0, 3):
    nummatriz.append(int(input('Digite um Numero: ')))
    matriz_1_2.append(nummatriz[:])
    nummatriz.clear()
for c in range(0, 3):
    nummatriz.append(int(input('Digite um Numero: ')))
    matriz_2_2.append(nummatriz[:])
    nummatriz.clear()
print(*matriz_0_2)
print(*matriz_1_2)
print(*matriz_2_2)
