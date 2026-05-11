# Implementar Lista Encadeada Simples em python Crie as classes Node e LinkedList. Implemente: inserção no início, inserção no final, remoção por valor, busca por valor e exibição de todos os elementos. Os nós não devem ser armazenados de forma

class no:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def __repr__(self):
        return f"No({self.valor})"
    
    
class Lista:
    def __init__(self):
        self.head = None
    
    def inserir_incio(self, valor):
        novo_no = no(valor)
        novo_no.proximo = self.head
        self.head = novo_no

    def inserir_final(self, valor):
        novo_no = no(valor)
        
        if self.head is None:
            self.head = novo_no
            return        
        
        no_atual = self.head
        while no_atual.proximo is not None:
            no_atual = no_atual.proximo
        no_atual.proximo = novo_no

    def remover(self, valor):
        if self.head is None:
            return False
        
        if self.head.valor == valor:
            self.head = self.head.proximo
            return True
        
        no_anterior = self.head
        no_atual = self.head.proximo
        while no_atual is not None:
            if no_atual.valor == valor:
                no_anterior.proximo = no_atual.proximo
                return True
            no_anterior = no_atual
            no_atual = no_atual.proximo
        return False
    
    def localizar_no(self, valor):
        if self.head is None:
            return None, -1
        
        posicao = 0
        no_atual = self.head
        while no_atual is not None:
            if no_atual.valor == valor:
                return no_atual, posicao
            no_atual = no_atual.proximo
            posicao += 1

        return None, -1
    
    def exibir(self):
        if self.head is None:
            return "head : None"
        
        valores = []
        no_atual = self.head
        while no_atual is not None:
            valores.append(f'[{no_atual.valor}]')
            no_atual = no_atual.proximo
        return "head : " + " → ".join(valores) + " → None" 


# l1 = Lista()
# l1.inserir_incio(15)
# l1.inserir_incio(17)
# l1.inserir_final(9)
# print(l1.exibir())

# l1.remover(12)
# l1.remover(15)
# print(l1.exibir())

# print("\n-Localizar nós-")
# no, posicao = l1.localizar_no(12)
# print(f'{no}, {posicao}')
# no, posicao = l1.localizar_no(9)
# print(f'{no}, [{posicao}]')
# no, posicao = l1.localizar_no(17)
# print(f'{no}, [{posicao}]')