


def voto(ano):
    """
    Programa pra verificação de possibilidade de votação
    :param ano: ano de nascimento
    :return: Condição perante a pessoa se encontra
    """
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif idade <18 or idade > 65:
        return f'Com {idade} anos: Voto Opcional'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO'


print(voto(int(input('Ano de Nascimento: '))))
