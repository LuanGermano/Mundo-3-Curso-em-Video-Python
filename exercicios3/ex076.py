# Crie um programa que tenha uma Tupla unica com nomes de produtos e seus respectivos preços na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''Dá para fazer em 2 linhas...
for i in range(0, len(prod), 2):
    print(f'{prod[i]:.<30}R${prod[i + 1]:7.2f}')'''


produtos = ('caneta', 2, 'Relogio', 23, 'remedio', 12, 'mouse', 10,
            'pão', 2, "mascara", 3, "gabinete", 245, "alcool", 11)
print(f'{"Listagem de preços":^30}') # Centralizando o topo
for i in range(0, len(produtos), 2): # FAZENDO O PRINT DAS INFORMAÇÕES COM FOR PULANDO DE 2 EM 2 PRA PEGAR A ORDEM CORRETA
    print(f'{str(produtos[i]).upper():.<24}', end='')  # TRANSFORMADO EM STR, CENTRALIZADO A DIREITA COM PONTO ENCHENDO O ESPAÇO
    print(f'R${produtos[i+1]:>6.2f} ')  # ADICIONADO 1 NO INDICE PRA COMEÇAR DO SEGUINTE E MSOTRAR TODOS OS PREÇOS.
