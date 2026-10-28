from chave import criar_chave

def registrar_chegada (arvore, data, horario, linha):
    valor = (data, horario, linha)
        
    resultado = arvore.inserir(valor)
        
    if resultado:
        return "OK"
    else: 
        return "DUPLICADO"
