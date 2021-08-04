# Reescreva a função LEIAINT() da aula 104, incluindo agora a possibilidade da digitação de um numero invalido
# Aproveite e crie a função LEia FLoat com a msm funcionalidade

def leiaint():
    """
    Programa de validação de numeros inteiros.
    :return:
    """
    while True:
        try:
            n = int(input("Digite um valor numerico Inteiro: "))
        except (ValueError, TypeError):
            print('\033[31mTivemos um problema com o tipo do dado inserido, coloque-o novamente.\033[m')
        except KeyboardInterrupt:
            print('O Usuario não digitou nada:')
        else:
            print(f'Voce digitou o Numero {n}')
            return n


def leiafloat():
    """
        Programa de validação de numeros reais.
        :return:
        """
    while True:
        try:
            n = float(input("Digite um valor numerico Real: "))
        except (ValueError, TypeError):
            print('\033[31mTivemos um problema com o tipo do dado inserido, coloque-o novamente.\033[m')
        except KeyboardInterrupt:
            print('O Usuario não digitou nada:')
        else:
            print(f'Voce digitou o Numero {n}')
            return n


i = leiaint()
f = leiafloat()
print(f'Os numeros digitados foram {i} e {f}')