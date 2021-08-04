numeros = list()
while True:
    n = int(input('Digite um Valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor já inserido')
    r = str(input('Deseja continuar?[S/N] '))
    if r in 'Nn':
        break
numeros.sort()
print('A Lista de valores é: ', end='')
print(*numeros, sep=', ')