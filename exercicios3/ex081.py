# Crie um programa que vai ler varios numeros e colocar em uma lista. Dpois mostre:
'''
A) Quantos numeros foram digitados
B) A lista de valores, Ordenada de forma descrescente.
C)Se o valor 5 foi digitado e esta ou nao na lista
'''

valores = []
while True:
    num = int(input('Digite um Valor: '))
    valores.append(num)
    resp = str(input('Deseja continuar?[S/N] ')).strip()
    while resp not in 'SsNn':
        resp = str(input('Deseja continuar?[S/N] ')).strip()
    if resp in 'Nn':
        break

valores.sort(reverse=True)
print(f'A) Foram digitados {len(valores)} numeros ')
print(f'B) A lista dos valores é: \033[34m', end='')
print(*valores, sep=", ")
if valores.count(5) == 0:
    print(f'\033[mC) O valor 5 não foi digitado. ')
else:
    print(f'\033[mC) O valor 5, esta na lista e foi digitado {valores.count(5)} vezes')
