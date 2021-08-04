#Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero ate vinte.
#Seu programa deverá ler um numero pelo teclado e mostra-lo por extenso.
# só catar o numero gerado e botar dentro do indice

extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze','Treze', 'Catorze', 'Quinze', 'Dezesseis','Dezessete',
           'Dezoito','Dezenove','Vinte')

while True:
    num = ''
    while num not in range(0,20):
        num = int(input('Digite um valor de 0 a 20: '))
    print(f'O seu numero {num} por extenso é {extenso[num]}')
    cont = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if cont == "N":
        break
