from chave import criar_chave

def buscar_chegada(arvore, data, horario, linha):
    return arvore.buscar(criar_chave(data, horario, linha))
