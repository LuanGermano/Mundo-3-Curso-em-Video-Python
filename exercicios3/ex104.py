# Crie um programa que tenha a função LEIAINT(), que vai funcionar de forma semelhante a função INPUT()
# só que fazendo a validação para aceitar apenas um valor numericos
# Ex: n = leiaint('digite um n')

def leiaint():
    """
    Programa de validação de numeros inteiros.
    :return:
    """
    while True:
        n = str(input("Digite um valor numerico: "))
        if n.isnumeric():
            n = int(n)
            break
    print(f'Voce digitou o Numero {n}')


leiaint()
