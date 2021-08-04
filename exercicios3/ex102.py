# Crie um programa que tenha uma função FATORIAL que receba dois parametros:
# O primeiro que sera o NUMERO a calcular e o outro chamado show, que sera um valor LOGICO
# indicando se sera mostrado ou nao na tela o processo de calculo do fatorial.
def fatorial(a, show=''):
    """
    Programa que serve pra realizar uma contagem fatorial
    :param a: o valor calculado
    :param show: Se deseja ver os numeros que compoem o fatorial(opcional)
    :return: retorno do valor de fatorial a.
    """
    from time import sleep
    f = 1
    print(f'O fatorial de {a}! é: ', end='')
    for c in range(a, 0, -1):
        f *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(end=' x ')
                sleep(0.24)
            else:
                print(end='= ')
                sleep(0.24)
    return print(f)


fatorial(int(input('Digite um valor que deseja para fatorial: ')),
         str(input('Deseja ver a conta sendo realizada:[deixe vazio caso n queira] ')).strip().title())

