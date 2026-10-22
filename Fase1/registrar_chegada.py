from busca_binaria import Arvore, No

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