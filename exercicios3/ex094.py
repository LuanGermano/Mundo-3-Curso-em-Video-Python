# Crie um programa que leia NOME, SEXO e IDADE de varias pessoas,
# guardando os dados em um dicionario e todos numa lista
# No final, mostre:
'''
A) Quantas pessoas foram cadastradas
B) A média de idade do grupo
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.
'''

pessoas = []
pessoa = {}
mulher = []
media = []
acima = []
while True:
    pessoa['pessoa'] = str(input('Nome: ')).strip().title()  # adição de chave e valor pro dict
    pessoa['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()  # adição de chave e valor pro dict
    while pessoa['sexo'] not in "MF":  # condição de controle pra garantir resposta aceita pelo programa
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()
    if pessoa['sexo'] == 'F':  # Caso seja um F ira adicionar o nome na lista separada pra mulheres.
        mulher.append(pessoa['pessoa'])
    pessoa['idade'] = int(input('Idade: '))   # adição de chave e valor pro dict
    media.append(pessoa['idade'])  # pegar os valores de idade pra serem postos na lista que servira pra media.
    pessoas.append(pessoa.copy())  # adição na lista geral.
    continuar = str(input('Deseja continuar?[S/N] ')).upper()
    while continuar not in 'SN':  # condição de controle pra garantir resposta dentro do que o programa entende
        continuar = str(input('Deseja continuar?[S/N] ')).upper()
    if continuar == 'N':  # Condição de parada pra repetição eterna
        break
med = sum(media) / len(media)  # media das idades
print(f'A) foram cadastradas {len(pessoas)} pessoas. ')
print(f'B) A média de idade do grupo é de {med:5.2f} anos')
print(f'C) As mulheres presentes na lista são: ', end='')
print(*mulher, sep=', ')
print(f'D) As pessoas com idade maior que a média são: ')
for n, i in enumerate(pessoas):  # Para cada pessoa na lista, compara a idade dela com a media estabelecida
    if pessoas[n]['idade'] >= med:  # se for maior, sera impressa no final
        print(pessoas[n]['pessoa'], end='; ')
        print(f'Sexo {pessoas[n]["sexo"]}; com {pessoas[n]["idade"]} anos.')

# no acima poderia ter feito assim
'''
for n, i in enumerate(pessoas):  # Para cada pessoa na lista, compara a idade dela com a media estabelecida
    if i['idade'] >= med:  # se for maior, sera impressa no final
        print(i['pessoa'], end='; ')
        print(f'Sexo {i["sexo"]}; com {["idade"]} anos.')
'''