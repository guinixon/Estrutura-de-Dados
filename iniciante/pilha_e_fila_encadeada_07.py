from lista_encadeada_06 import Lista
from lista_encadeada_06 import no


class PilhaEncadeada(Lista):
    def __init__(self):
        self.head = None
    
    def push(self, valor):
        self.inserir_incio(valor)

    def pop(self):
        if self.head is None: 
            return False
        
        valor_removido = self.head.valor
        self.head = self.head.proximo
        return valor_removido
    
class FilaEncadeada(Lista):
    def __init__(self):
        self.head = None

    def enqueue(self, valor):
        self.inserir_final(valor)

    def dequeue(self):
        if self.head is None:
            return False
        
        valor_removido = self.head
        self.head = self.head.proximo
        return valor_removido
