class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class LinkedList:
    def __init__(self):
        self.header = None
        

    def inserir_inicio(self, valor):
        posicao = Node(valor)
        posicao.proximo = self.header
        self.header = posicao

    def final(self, valor):
        posicao = Node(valor)
        if self.header is None:
            self.header = posicao
            return
        else:
            atual = sel.header
            while posicao.proximo is not None:
                posicao.atual = posicao.proximo
            