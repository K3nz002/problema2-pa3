class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

class Arvore:
    def __init__(self):
        self.raiz = None
        
    def inserir(self, valor):
        if self.raiz is None:  # se a árvore está vazia, insere o valor na raiz
            self.raiz = No(valor)
            return True
        return self._inserir(self.raiz, valor)
    
    def _inserir(self, no, valor):
        if valor == no.valor:
            return False  # Chegada duplicada
        elif valor < no.valor:  # valor menor vai para a esquerda
            if no.esq is None:
                no.esq = No(valor)
                return True
            return self._inserir(no.esq, valor)
        else:  # valor maior vai para a direita
            if no.dir is None:
                no.dir = No(valor)
                return True
            return self._inserir(no.dir, valor)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, no, valor):
        if no is None:  # valor não encontrado
            return False
        if valor == no.valor:  # valor encontrado
            return True
        elif valor < no.valor:  # valor menor vai para a esquerda
            return self._buscar(no.esq, valor)
        else:
            return self._buscar(no.dir, valor)

    def menor_valor(self, no):
        atual = no
        while atual.esq is not None: 
            atual = atual.esq
        return atual.valor

    def remover(self, valor): 
        self.raiz, removido = self._remover(self.raiz, valor)
        return removido
    
    def _remover(self, no, valor):
        if no is None:
            return None, False

        removido = False
        if valor < no.valor:
            no.esq, removido = self._remover(no.esq, valor)
        elif valor > no.valor:
            no.dir, removido = self._remover(no.dir, valor)
        else:  # valor encontrado
            removido = True
            # Nenhum filho ou apenas um filho
            if no.esq is None:
                return no.dir, True
            elif no.dir is None:
                return no.esq, True

            # Dois filhos - substitui pelo sucessor (menor nó da subárvore direita)
            sucessor_valor = self.menor_valor(no.dir)
            no.valor = sucessor_valor
            no.dir, _ = self._remover(no.dir, sucessor_valor)

        return no, removido

    def em_ordem(self):
        resultado = []
        def _percorrer(no):
            if no is not None:
                _percorrer(no.esq)
                resultado.append(no.valor)
                _percorrer(no.dir)
        _percorrer(self.raiz)
        return resultado