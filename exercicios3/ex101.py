# Crie um programa que tenha uma função chamada VOTO
# Que vai receber de PARAMETRO o ano de nascimento de uma pessoa,
#Retornando se a pessoa é NEGADA, OPCIONAL OU OBRIGATORIA, nas eleições.
from datetime import date
year = date.today().year


def voto(ano):
    """
    Programa pra verificação de possibilidade de votação
    :param ano: ano de nascimento
    :return: Condição perante a pessoa se encontra
    """
    if idade >= 16 or idade <= 65:
        v = 'Opcional'
    if idade > 18:
        v = 'Obrigatorio'
    else:
        v = 'Não vota'
    return print(f"vc tem {idade} e seu voto é {v}")


ano = int(input('Qual o seu ano de nascimento: '))
idade = year - ano
voto(ano)
