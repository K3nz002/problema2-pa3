from arvore_avl import *
from chave import para_segundos, chave_para_chegada
from buscar_index_linha import obter_arvore_da_linha

def proximo_da_linha(linhas_arvores, data, hora, linha):

    arvore = obter_arvore_da_linha(linhas_arvores, linha, nao_existe=False)
    if arvore is None or arvore.raiz is None:
        return None

    melhor = None
    instante = para_segundos(data, hora)
    atual = arvore.raiz

    while atual is not None:
        if atual.valor[0] >= instante:
            melhor = atual.valor
            atual = atual.esq
        else:
            atual = atual.dir

    if melhor is None:
        return None
    data_r, hora_r, _ = chave_para_chegada(melhor)
    return (data_r, hora_r)
