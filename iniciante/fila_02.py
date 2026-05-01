from collections import deque

class Fila():
    def __init__(self):
        self.dados = []

    def enqueue(self, item):
        return self.dados.append(item)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Error: fila vazia")
        return self.dados.pop(0)
    
    def front(self):
        if self.is_empty():
            raise IndexError("Error: fila vazia")
        return self.dados[0]
    
    def is_empty(self):
        return len(self.dados) == 0
    
    def __repr__(self):
        return f'{self.dados}'
    

class FilaDeque():
    def __init__(self):
        self.dados = deque()

    def enqueueDeque(self, item):
        return self.dados.append(item)
    
    def dequeueDeque(self):
        if self.is_emptyDeque():
            raise IndexError("Error: fila vazia")
        return self.dados.popleft()
    
    def frontDeque(self):
        if self.is_emptyDeque():
            raise IndexError("Error: fila vazia")
        return self.dados[0]
    
    def is_emptyDeque(self):
        return len(self.dados) == 0
    
    def __repr__(self):
        return f'{self.dados}'

f = Fila()
print(f)
print(f'Is empty? {f.is_empty()}')



f.enqueue(10)
f.enqueue(6)
f.enqueue(12)
f.enqueue(9)
print(f"Primeiro item da fila: {f.front()}")
print(f)
print(f'Is empty? {f.is_empty()}')

f.dequeue()
print(f)

print("\n-- FILA COM DEQUE --\n")
## -- Fila reimplementada com Deque

f1 = FilaDeque()
print(f1)
print(f'Is empty? {f1.is_emptyDeque()}')


f1.enqueueDeque(9)
f1.enqueueDeque(2)
f1.enqueueDeque(17)
f1.enqueueDeque(1)
print(f"Primeiro item da fila Deque: {f1.frontDeque()}")
print(f1)
print(f'Is empty? {f1.is_emptyDeque()}')

f1.dequeueDeque()
print(f1)