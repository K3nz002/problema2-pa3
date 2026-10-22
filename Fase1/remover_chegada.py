from chave import criar_chave
from busca_binaria import Arvore, No

def remover_chegada(arvore, data, horario, linha):
    return arvore.remover(criar_chave(data, horario, linha))
