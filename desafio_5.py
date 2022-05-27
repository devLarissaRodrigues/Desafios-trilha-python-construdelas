# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).
# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.


numero = -1
indice = -1

while numero < 60:
    numero += 1
    if numero % 2 != 0:
        print(f"Índice: {indice}| Item: {numero}")
    indice += 1





