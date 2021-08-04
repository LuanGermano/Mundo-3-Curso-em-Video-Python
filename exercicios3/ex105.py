# Faça um programa que tenha uma função NOTAS()
# que pode receber varias notas de alunos e vai retornar um dicionario
# Adicione docstrings
"""
- quantidade de notas
- a maior nota
- a menor nota
- a media da turma
- a situação(opcional)
"""
alunos = []


def linha():
    """
    Programa de linha.
    :return:
    """
    print('-=' * 20)


def notas(notas=1):
    """
    Programa para adicionar o aluno dentro da lista principal de alunos
    :param notas: Numero de notas que serão colocadas
    :return: Não possui
    """
    while True:
        aluno = {}
        nota = list()
        aluno['Nome'] = str(input('Nome do Aluno: ')).capitalize().strip()
        for c in range(0, notas):
            nota.append(float(input(f"Nota da materia {c + 1}: ")))
        aluno['Notas'] = nota[:]
        aluno["Maior"] = max(nota)
        aluno["Menor"] = min(nota)
        aluno["Media"] = sum(nota) / len(nota)
        if aluno["Media"] >= 7:
            aluno["Situação"] = "Boa"
        elif aluno["Media"] >= 5:
            aluno["Situação"] = "Mediana"
        else:
            aluno["Situação"] = "Ruim"
        nota.clear()
        alunos.append(aluno.copy())
        continuar = str(input('Deseja adicionar mais algum aluno?[S/N] ')).strip().upper()
        while continuar not in 'SN':
            continuar = str(input('Deseja adicionar mais algum aluno?[S/N] ')).upper().strip()
        if continuar == "N":
            break
        linha()

def perguntas(d):
    """
    Programa auxiliar pra leitura dos dados na lista de Alunos.
    :param d: Conferir se deseja saber a situação que o aluno se encontra
    :return: não possui
    """
    for num, dic in enumerate(alunos):
        for chave, valor in dic.items():
            if chave == "Nome":
                print(f'O Aluno: {valor},', end=' ')
            if chave == "Notas":
                print(f'Obteve as Notas: ', end='')
                print(*valor, sep=', ')
            if chave == "Maior":
                print(f'Sua maior nota foi {valor} e', end=' ')
            if chave == "Menor":
                print(f'sua menor nota foi {valor}')
            if chave == "Media":
                print(f'A média do Aluno {alunos[num]["Nome"]} é {valor:.2f}', end=' ')
                if d == False:
                    print()
            if d:
                if chave == "Situação":
                    print(f'e sua situação é: {valor}')
        linha()


n = int(input("Digite quantas notas serão avaliadas: "))
d = str(input("Deseja ver a situação do Aluno?[S/N] ")).strip().upper()
linha()
if d == "S":  # COLOCAR A SITUAÇÃO INDENPDENENTE, SÓ Q SE SIM APARECE NO FINAL
    d = True
else:
    d = False
notas(n)
linha()
perguntas(d)
