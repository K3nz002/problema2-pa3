class No:
    def __init__ (self, data, hora, linha):
        self.data = data
        self.hora = hora
        self.linha = linha
       
        self.esquerda = None
        self.direita = None
       
    def chave(self):
        return(self.data, self.hora, self.linha)
       
  class BuscaBinaria:
    def __init__ (self):
        self.raiz = None
       
    def registrar_chegada (self, data, hora, linha):
        novo_no = No (data, hora, linha)
        nova_chave = novo_no.chave()
       
        #arvore vazia
        if self.raiz is None:
            self.raiz = novo_no
            return "OK"
           
        atual = self.raiz
       
        while True:
            chave_atual = atual.chave()
           
            #chegada ja registrada
            if nova_chave == chave_atual:
                return "JÁ REGISTRADO"
               
            #chegada menor
            elif nova_chave < chave_atual:
                if atual.esquerda is None:
                    atual.esquerda = novo_no
                    return "OK"
                atual = atual.esquerda
                   
            #chegada maior
            else:
                if atual.direita is None:
                    atual.direita = novo_no
                    return "OK"
                atual = atual.direita
               
    def buscar_chegada (self, data, hora, linha):
        chave_busca = (data, hora, linha)
        atual = self.raiz
       
        while atual is not None:
            chave_atual = atual.chave()
           
            if chave_busca == chave_atual:
                return "ACHOU"
               
            elif chave_busca < chave_atual:
                atual = atual.esquerda
               
            else:
                atual = atual.direita
               
        return "NAO"     
