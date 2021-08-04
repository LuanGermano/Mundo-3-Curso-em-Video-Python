aluno = {}
alunos = []
while True:
    aluno['Aluno'] = str(input('Digite o nome do aluno: ')).title()  # valor pro dicionario
    aluno['media'] = float(input(f'Media do aluno {aluno["Aluno"]}: '))  # valor pro dicionario
    if aluno['media'] <= 5:  # Programa comparativo pra definir qual a situação ira preencher o dicionario
        aluno['situação'] = 'Reprovado'
    elif aluno['media'] <= 7:
        aluno['situação'] = 'Recuperação'
    else:
        aluno['situação'] = 'Aprovado'
    alunos.append(aluno.copy())  # Copia do dicionario pra dentro da lista
    continuar = str(input('Deseja adicionar mais algum aluno?[S/N] ')).upper()  # Verificação de continuação
    while continuar not in 'SN':
        continuar = str(input('Deseja adicionar mais algum aluno?[S/N] ')).upper()
    if continuar == "N":
        break
print('=-=' * 12)
for dicionario in alunos:  # Para cada item dentro da lista de alunos
    for chave, atribuição in dicionario.items():  # para cada chav e valor dentro dos items do dicionario
        print(f'-{chave}: {atribuição}')  # minha resposta da solicitação
    print()
    print('=-=' * 12)
