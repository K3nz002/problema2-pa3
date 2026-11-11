class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        self.altura = 1

class Arvore:
    def __init__(self):
        self.raiz = None
        
    def altura(self, no):
        if no is None:
            return 0
        return no.altura
        
    def fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.altura(no.esq) - self.altura(no.dir)
        
    def atualizar_altura(self, no):
        no.altura = 1 + max(
            self.altura(no.esq), self.altura(no.dir)
        )
        
    def rotacao_direita(self, y):
        x = y.esq
        t2 = x.dir

        # Realiza rotação
        x.dir = y
        y.esq = t2

        # Atualiza alturas
        self.atualizar_altura(y)
        self.atualizar_altura(x)

        # Retorna novo nó raiz da subárvore
        return x

    def rotacao_esquerda(self, x):
        y = x.dir
        t2 = y.esq

        # Realiza rotação
        y.esq = x
        x.dir = t2

        # Atualiza alturas
        self.atualizar_altura(x)
        self.atualizar_altura(y)

        # Retorna novo nó raiz da subárvore
        return y
        
    def balancear(self, no):
        if no is None:
            return no
        
        self.atualizar_altura(no)
        fb = self.fator_balanceamento(no)
        
        # Caso LL
        if fb > 1 and self.fator_balanceamento(no.esq) >= 0:
            return self.rotacao_direita(no)
        
        # Caso LR
        if fb > 1 and self.fator_balanceamento(no.esq) < 0:
            no.esq = self.rotacao_esquerda(no.esq)
            return self.rotacao_direita(no)
        
        # Caso RR
        if fb < -1 and self.fator_balanceamento(no.dir) <= 0:
            return self.rotacao_esquerda(no)
        
        # Caso RL
        if fb < -1 and self.fator_balanceamento(no.dir) > 0:
            no.dir = self.rotacao_direita(no.dir)
            return self.rotacao_esquerda(no)
        
        return no
        
    def inserir(self, valor):
        self.raiz, inserido = self._inserir(self.raiz, valor)
        return inserido
    
    def _inserir(self, no, valor):
        if no is None:
            return No(valor), True
        
        if valor == no.valor:
            return no, False  # Valor duplicado
        elif valor < no.valor:
            no.esq, inserido = self._inserir(no.esq, valor)
        else:
            no.dir, inserido = self._inserir(no.dir, valor)
        
        return self.balancear(no), inserido

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

        return self.balancear(no), removido

    def em_ordem(self):
        resultado = []
        self._percorrer(self.raiz, resultado)
        return resultado
    
    def _percorrer(self, no, resultado):
        if no is None:
            return
        
        self._percorrer(no.esq, resultado)
        resultado.append(no.valor)
        self._percorrer(no.dir, resultado)