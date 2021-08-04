# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla
'''
A) quantas vezes apareceu o valor 9.
B)Em que posição foi digitado o primeiro valor 3.
C) Quais foram os numeros PAres.

'''
v1 =int(input('Digite um valor: '))
v2 =int(input('Digite um Valor: '))
v3 =int(input('Digite um Valor: '))
v4 =int(input('Digite um Valor: '))
valores = (v1, v2, v3, v4)
cont = 0
print(valores)
print(f'O maior valor é de {max(valores)}')
if 3 in valores:
    print(f'O primeiro valor 3 ta na {valores.index(3)+1}ª posição ')
for num in valores:
    if num % 2 == 0:
        cont += 1
print(f'Tem valores {cont} pares ')