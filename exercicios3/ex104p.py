def leiaint(msg):
    """
    Codigo pra validação de numero inteiro
    :param msg: Valor recebido
    :return: A int do Numero digitado.
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Numero invalido.\033[m')
        if ok:
            break
    return valor


n = leiaint("Digite um numero: ")
print(f'Voce acabou de digitar o numero {n}')