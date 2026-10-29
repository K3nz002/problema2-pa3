from chave import criar_chave

def remover_chegada(arvore, data, horario, linha):
    return arvore.remover(criar_chave(data, horario, linha))
