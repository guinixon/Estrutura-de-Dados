# Dada uma pilha P1 com números inteiros aleatórios, use uma pilha auxiliar P3 para separar os elementos em P1 (ímpares) e P2 (pares), deixando P3 vazia ao final.
def par_impar(p1):
    p2 = []
    p3 = []
    while p1:
        p3.append(p1.pop())
    while p3:
        numero = p3.pop()
        if numero % 2 == 0:
            p1.append(numero)
        else:
            p2.append(numero)
            
    return f'Pares: {p1}\nImpares: {p2}'

p1 = []
print(par_impar(p1))