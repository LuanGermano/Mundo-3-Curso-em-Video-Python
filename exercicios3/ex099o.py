def linha():
    print('-=' * 14)


def maior(*num):
    mai = 0
    print(f'Possui {len(num)} valores \nA lista de numeros é:', end=' ')
    for v in num:
        print(v, end=' ')
        if mai < v:
            mai = v
    print()
    print(f'O maior numero da lista é {mai}')
    linha()


maior(2, 3, 6, 2312, 45, 67)
maior(3, 4, 7, 2, 11, 55)
