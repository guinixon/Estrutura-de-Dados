def inverta_com_pila(Lista):
    pilha = []
    pilha_inversa = []

    for n in Lista:
        pilha.append(n)

    while pilha:
        pilha_inversa.append(pilha.pop())

    return pilha_inversa

entrada = input("Digite números separados por espaço: ")
numeros = entrada.split()

print(inverta_com_pila(numeros))