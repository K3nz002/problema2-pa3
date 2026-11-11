from arvore_avl import *
from chave import criar_chave
from buscar_index_linha import obter_arvore_da_linha

def remover_chegada(arvore, linhas_arvores, data, horario, linha):
    chave = criar_chave(data, horario, linha)
    removido = arvore.remover(chave)
    if removido:
        arvore_linha = obter_arvore_da_linha(linhas_arvores, linha, nao_existe=False)
        if arvore_linha is not None:
            arvore_linha.remover(chave)
    return removido
