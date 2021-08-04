from cor import cores
from time import sleep


def linha():
    print(f'{cores["pur"]}-{cores["cle"]}' * 42)


def leiaint(msg):
    """
    Programa pra leitura de inteiros
    :param msg: numero inteiro recebido pra avaliação
    :return: o valor pra fora
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cores["Bred"]}DADO INSERIDO INVALIDO. POR FAVOR COLOQUE-O NOVAMENTE{cores["cle"]}')
        except KeyboardInterrupt:
            print('O Usuario não digitou nada:')
        else:
            return n


def menu():
    linha()
    while True:
        print(f'{cores["Bgre"]}1 - VER PESSOAS CADASTRADAS')
        print('2 - NOVO CADASTRO')
        print(f'3 - SAIR{cores["cle"]}')
        linha()
        sleep(0.5)
        opcao = leiaint("Digite uma das opções: ")
        if opcao == 1 or opcao == 2 or opcao == 3:
            break
        else:
            print(f'{cores["Bred"]}NUMERO INVALIDO{cores["cle"]}')
            linha()
    linha()
    return opcao


def cadastro():
    """
    Programa pra cadastro de pessoas num deicionario
    :return: Retorna a pessoa cadastrada.
    """
    nome = str(input(f'{cores["Bblu"]}Nome: ')).strip().capitalize()
    idade = leiaint(f'Idade: {cores["cle"]}')
    # arquivo de texto
    pessoas = open('cadastro.txt', "a")
    pessoas.write(f'{nome}',)
    pessoas.write(str(f'\t\t\t\t{idade}'))
    pessoas.write(" Anos\n")
    pessoas.close()




