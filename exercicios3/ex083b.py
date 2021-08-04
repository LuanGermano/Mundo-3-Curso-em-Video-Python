expr = str(input("Digite uma expressão:"))
pilha = 0
for cont in expr:
    if cont == "(":
        pilha += 1  # Para cada parenteses aberto é somado 1
    if cont == ")":
        pilha -= 1  # Para cada parenteses Fechado é subtraido 1
    if pilha < 0:  # Se o numero da pilha for negativo significa que foi fechado um parenteses antes de abrir
        break  # Programa encerra no erro
if pilha == 0:  # Qualquer valor diferente de zero significa que a conta não fechou corretamente
    print("Sua expressão é valida!!!")
else:
    print("Sua expressão é invalida!!!")
