def linha():
    print('-' * 35)


def moeda(n):
    return f'R${n:.0f},00'


def aumentar(n, porce, q=False):
    if q:
        return moeda(n * (1 + porce/100))
    else:
        return n * (1 + porce/100)


def diminuir(n, porce, q=False):
    if q:
        return moeda(n * (1 - porce/100))
    else:
        return n * (1 - porce/100)


def dobro(n, q=False):
    if q:
        return moeda(n * 2)
    else:
        return n * 2


def metade(n, q=False):
    if q:
        return moeda(n / 2)
    else:
        return n / 2


def resumo(valor=1, aumento=0, desconto=0, form=True):
    linha()
    print(f'{"Preço Analisado: ":.<8} ', end='')
    print(f'{moeda(valor):<14}')

    print(f'{"Dobro do Preço: ":.<24} ', end='')
    print(f'{dobro(valor, form):<14}')

    print(f'{"Metade do preço: ":.<24} ', end='')
    print(f'{metade(valor, form):<14}')

    print(f'{aumento}% de Aumento: ', end=f'{"":<26} ')
    print(f'{aumentar(valor, aumento, form):<14}')

    print(f'{desconto}% de Desconto: ', end=f'{"":<26} ')
    print(f'{diminuir(valor, desconto, form):<14}')
    linha()
