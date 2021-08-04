# programa do professor pro mesmo problema, é mais simples pois quando eu fiz coloquei pra aceitar mais pessoas.

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'media de {aluno["nome"]}:'))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media']:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'- {k} é igual a {v}.')
