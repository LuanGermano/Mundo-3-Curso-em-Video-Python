# Crie um programa que leia, NOME, NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os(com idade) em um dicionario
# Se por acaso a CTPS for diferente de ZERO, o dicionario receberá tambem o ANO DE CONTRATAÇÃO e o Salario.
# Calcule e acrescente, alem da idade, com quantos anos a pessoa vai se aposentar;
# PORRA DE EXERCICIO
# considere 35 anos de contribuição
from datetime import date
year = date.today().year  # Importação de ano atual do programa
pessoa = dict()

pessoa['Nome'] = str(input('Nome: ')).title().strip()  # adição de chave e valor pro dict
idade = int(input('Ano de nascimento: '))  # verificação de ano
pessoa['Idade'] = year - idade  # verificação de idade considerando somente o ano de nascimento; traz erros
pessoa['CTPS'] = int(input('Numero da carteira de trabalho: '))  # adição de chave e valor pro dict
if pessoa['CTPS'] != 0:  # verificação se a carteira de trabalho existe
    pessoa['Ano de contratação'] = int(input('Ano de contratação: '))
    pessoa['Salario'] = float(input('Salario atual: '))
    pessoa['Aposentadoria'] = (pessoa['Ano de contratação'] - idade) + 35

for k, v in pessoa.items():
    print(f'{k}: {v}')

