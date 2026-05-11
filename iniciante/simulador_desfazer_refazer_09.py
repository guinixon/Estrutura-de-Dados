class editorTexto:
    def __init__(self):
        self.pilha_historico = []
        self.pilha_refazer = []

    def escrever(self, texto):
        self.pilha_historico.append(texto)
        self.pilha_refazer.clear()
        print(f'Texto: "{texto}"')
    
    def desfazer(self):
        if not self.pilha_historico:
            print("Sem texto")
            return
        self.pilha_refazer.append(self.pilha_historico.pop())
        return self.pilha_historico[-1]

    def refazer(self):
        if not self.pilha_refazer:
            print("Sem texto")
            return
        self.pilha_historico.append(self.pilha_refazer.pop())
        return self.pilha_historico
    
    def exibir(self):
        if not self.pilha_historico :
            return f'vazio'
        
        atual = self.pilha_historico[-1]
        return f'Texto: {atual}'


e1 = editorTexto()
e1.escrever("Olá mundo")
e1.escrever("Eu amo Python")
e1.escrever("Sou Guilherme")
print(e1.exibir())
e1.desfazer()
print(e1.exibir())
e1.desfazer()
print(e1.exibir())
e1.refazer()
print(e1.exibir())
e1.refazer()
print(e1.exibir())