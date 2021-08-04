# Msm bosta dos anteriores, Depois disso, crie duas listas extras pra PAR e IMPAr
# no fim mostre as 3 listas.
lista = []
lista_par = []
lista_impar = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    conti = str(input('Deseja continuar?[S/N] ')).upper()
    while conti not in 'SN':
        conti = str(input('Deseja continuar?[S/N] '))
    if conti == 'N':
        break
lista.sort()
for n in lista:
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
print(f'Os numeros são: ', end='')
print(*lista, sep=', ')
print(f'Os numeros Pares são: ', end='')
print(*lista_par, sep=', ')
print(f'Os numeros impares são: ', end='')
print(*lista_impar, sep=', ')
