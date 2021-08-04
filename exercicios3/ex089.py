# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta
# No final, mostre um boletim contendo a media de cada um e permita que o usuario
# Possa mostrar as notas individualmente.
# Faz assim
# Alunos = [alunos [Aluno [nota 1], [nota 2], [notamedia]], [Alunos[nota 1], [nota 2]]]
from time import sleep
alunos = []
aluno = []
while True:
    aluno.append(str(input('Nome do Aluno: ')).title())  # Nome do Aluno
    n1 = (float(input('Nota 1: ')))
    n2 = (float(input('Nota 2: ')))
    nm = (n1 + n2) / 2  # Media das notas
    aluno += n1, n2, nm  # Adicionando cada um dos resultados
    alunos.append(aluno[:])  # copia adicionada dentro da lista maior
    aluno.clear()  #Lista zerada pra novas informações
    conti = str(input('Deseja continuar?[S/N] ')).upper().strip()
    while conti not in 'SN':
        conti = str(input('DESEJA CONTINUAR?[S/N] ')).upper().strip()
    if conti == 'N':
        break
print('=-=' * 10)
print(f'{"Notas dos alunos":^24}')
print(f'{"No.":<4}{"NOME":<10}{"NOTA":>8}')
for cont, al in enumerate(alunos):
    print(f'[{cont}] {alunos[cont][0]:<10}', end=' ')  # Nome do aluno
    print(f'{alunos[cont][3]:>6}')  # Media do aluno
print('=-=' * 10)
while True:
    check = int(input('\nDeseja Ver algum aluno em especifico?[999 para parar]: '))  # Se deseja ver alguem em especifico
    if check not in range(0, len(alunos)) or check == 999:  # Ordem de parada do while
        print('Encerrando o programa...')
        sleep(0.5)
        break
    print(f'A nota do aluno {alunos[check][0]}:')
    print(f'Na máteria da nota 1 tirou {alunos[check][1]:.1f}\nNa materia da nota 2 tirou {alunos[check][2]:.1f}')

