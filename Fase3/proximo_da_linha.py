from arvore_avl import *
from chave import para_segundos, chave_para_chegada
from buscar_index_linha import obter_arvore_da_linha

# R4: PROXL data hora linha (Fase 1: percorre a árvore inteira)
def proximo_da_linha(linhas_arvores, data, hora, linha):
    
    arvore = obter_arvore_da_linha(linhas_arvores, linha, nao_existe=False)
    if arvore is None or arvore.raiz is None:
        return None
    
    melhor = None
    instante = para_segundos(data, hora)

    def percorrer(no):
        nonlocal melhor
        if no is None:
            return
        seg, lin = no.valor
        if lin == linha and seg >= instante:
            if melhor is None or seg < melhor[0]:
                melhor = no.valor
        percorrer(no.esq)
        percorrer(no.dir)

    percorrer(arvore.raiz)
    if melhor is None:
        return None
    data_r, hora_r, _ = chave_para_chegada(melhor)
    return (data_r, hora_r)
