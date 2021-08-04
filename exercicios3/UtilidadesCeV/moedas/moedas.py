def linha():
    print('-' * 35)


def moeda(n):
    return f'R${n:.2f}'.replace(".",",")


def aumentar(n, porce, q=False):
    if q:
        return moeda(n * (1 + porce/100))
    else:
        return n * (1 + porce/100)


def diminuir(n, porce, q=False):
    if q:
        return moeda(n * (1 - porce/100))
    else:
        return (n * (1 - porce/100))


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
    print(f'{"Preço Analisado: "} ', end='')
    print(f'\t{moeda(valor)}')

    print(f'{"Dobro do Preço: "} ', end='')
    print(f'\t{dobro(valor, form)}')

    print(f'{"Metade do preço: "} ', end='')
    print(f'\t{metade(valor, form)}')

    print(f'{aumento}% de Aumento:', end=f'')
    print(f'\t\t{aumentar(valor, aumento, form)}')

    print(f'{desconto}% de Desconto:', end=f'')
    print(f'\t{diminuir(valor, desconto, form)}')
    linha()
