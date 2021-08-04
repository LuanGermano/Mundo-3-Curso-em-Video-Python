def leiaDinheiro(msg):
    valor = 0

    while True:
        num = str(input(msg))
        if num[-1].isnumeric():
            num = num.replace(",", ".")
            valor = float(num)
            break
        else:
            print(f'\033[0;31mERRO! "{num}" é Numero invalido.\033[m')
    return valor
