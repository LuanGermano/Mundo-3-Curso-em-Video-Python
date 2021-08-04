listanum = []
posma = []
posme = []
mai = 0
men = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um Valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < mai:
            men = listanum[c]
print(*listanum, sep=', ')
for i, v in enumerate(listanum):
    if v == mai:
        posma.append(i)
    if v == men:
        posme.append(i)
print(f'O Maior valor é {mai} nas posições {posma} e o menor é {men} nas posições {posme}')
