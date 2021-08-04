# Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista
# Caso o Numero já exista la dentro, não sera adicionado. No Final mostre todos valores unicos Crescentes
# avise se o numero for repetido
valor = []
while True:
    continuar = 'n/a'
    val = int(input('Digite um valor: '))
    if val in valor:
        print('Valor repetido, não será adicionado')
    else:
        valor.append(val)
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar?[S/N] ')).upper()
    if continuar in 'N':
        break
valor.sort()
print(f'Os Numeros adicionados foram em ordem crescente ', end='')
print(*valor, sep=', ')