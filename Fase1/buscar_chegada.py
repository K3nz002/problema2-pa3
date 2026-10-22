from busca_binaria import Arvore, No

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