print('='*40)
n=int(input('Digite o valor de n da matriz n x n: '))
matriz = [[] for c in range(0, n)]
print(matriz)
for l in range(0, n):
    for c in range(0, n):
        matriz[l].append(int(input(f'Digite um valor para [{l},{c}]: ')))
print('-=' * 20)
for l in range(0, n):
    for c in range(0, n):
        print(f'[{matriz[l][c]:^7}]', end=' ')
    print()