from chave import criar_chave

def registrar_chegada(arvore, data, horario, linha):
    return arvore.inserir(criar_chave(data, horario, linha))
