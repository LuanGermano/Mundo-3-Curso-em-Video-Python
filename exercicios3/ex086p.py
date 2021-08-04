matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0, 3):
    for col in range(0, 3):
        matriz[l][col] = int(input(f'Digite o [{l}, {col}] da matriz: '))
print('--'*15)
for l in range(0, 3):
    for col in range(0, 3):
        print(f'[{matriz[l][col]:^7}]', end='')
    print()