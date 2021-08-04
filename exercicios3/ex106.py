# Faça um mini sistema que utilize o interctive help do Python.
# O usuario vai digitar o comando e o manual vai aparecer.
# quando o usuario digitar FIM encerre, USA CORES
from cor import cores
def ajuda(msg):
    pedido = str(input(msg))
    help(pedido)
    return pedido

def titulo(msg, cor=0):
    tam = len(msg) +4
    print(f'\033[0;31;40m')
    print('~' * tam)
    print(f'  {msg}')
    print('~'* tam)
    print(cores['cle'])



print('\033[0;31m')
while True:
    titulo(' Sistema de ajuda Pyhelp')
    i = ajuda("Qual comando vc deseja conhecer?\033[m ")
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == "N":
        break