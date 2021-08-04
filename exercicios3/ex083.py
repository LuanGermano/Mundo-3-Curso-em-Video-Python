# Esse vou fazer sozinho!(claro q naquelas né
# Crie um programa onde o usuario digite uma expressão qualquer que use parenteses.
# seu aplicativo deverá analisar se a expressão passada esta com os parenteses abertos e fechados na ordem correta.
# Ex de valida: ((A+B) * C)
# Ex de invalida: ((A+B) * C)) ||| ((a+b) * (a*c)- 2
# Bem, acho q comparando o numero de caracteres de parenteses deve funfar
# e se tiver na ordem inversa Luan? viu ce ta errado

equa = str(input('Digite uma expressão qualquer: '))
pilha = []
for simb in equa:
     if simb == '(':
        pilha.append('(')  # To adicionando um Item pra pilha significando q parenteses foram abertos.
     elif simb == ')':
         if len(pilha) > 0:
             pilha.pop()  # To excluindo o parentes adicionado cada vez q fecho um
         else:
             pilha.append(')')  # Se eu fechar um parenteses a mais do q foi aberto será adicionado na pilha
             break  # E o programa vai encerrar no mesmo problema pois já tem erro
print(pilha)
if len(pilha) == 0:  # Se sobrou qualquer valor dentro da pilha, estará errado.
    print('certo')
else:
    print('errado')
