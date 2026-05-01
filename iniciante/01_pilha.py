# Implementar uma Pilha do Zero
# Crie uma classe Pilha em Python sem usar bibliotecas externas. Ela deve ter os métodos push(item), pop(), peek(), is_empty() e size(). Valide cada método com testes.
# Acadêmico — USP/IME
# Dica: Internamente use uma lista Python. O topo da pilha é sempre o último elemento: self.dados[-1].


class Pilha:
    def __init__(self):
        self.dados = []
    
    def push(self, item):
        self.dados.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Erro: Lista vazia")
        return self.dados.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Erro: Lista vazia")
        return self.dados[-1]
    
    def is_empty(self):
        return len(self.dados) == 0
    
    def size(self):
        return len(self.dados) 
    
    def __repr__(self):
        return f"{self.dados}"

##Teste

p = Pilha()
print(p)
print(f"is empty? {p.is_empty()}")

p.push(10)
p.push(7)
p.push(8)
print(p)
print(f"is empty? {p.is_empty()}")

print(f"Removendo: {p.pop()}")
print(p)

print(f"Ultimo elemento adicionado a lista: {p.peek()}")
print(f"Tamanho atual da pilha: {p.size()}")