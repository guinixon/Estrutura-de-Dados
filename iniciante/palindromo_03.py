# Escreva uma função palindromo(s: str) -> bool que use sua classe Pilha para verificar se uma string é palíndromo, sem usar s[::-1] ou reversed().

from iniciante.pilha_01 import Pilha

def palindromo(s: str) -> bool:
    palavra = s.lower().replace(" ", "")
    caracteres = Pilha()
    reverso = Pilha()
    
    for letra in palavra:
        caracteres.push(letra)
        reverso.push(caracteres.pop())

    for letra in palavra:      
        caracteres.push(letra)
        if caracteres.pop() != reverso.pop():
            return False
    return True


print(palindromo("radar"))

