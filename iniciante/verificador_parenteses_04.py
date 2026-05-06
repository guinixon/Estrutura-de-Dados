# Dada uma expressão como "({[]})" ou "([)]", use uma pilha para determinar se os parênteses, colchetes e chaves estão corretamente balanceados. Retorne True ou False.
def verificador (expressao : str) -> bool:
    dicionario = {')':'(', ']':'[', '}':'{'}
    pilha = []
    for c in expressao:
        if c in dicionario.values():
            pilha.append(c)
        elif c in dicionario.keys():
            if len(pilha) == 0:
                return False
            if pilha[-1] == dicionario[c]:
                pilha.pop()
            else:
                return False
    if len(pilha) != 0:
        return False
    return True
print(verificador(''))