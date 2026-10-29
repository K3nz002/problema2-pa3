from chave import para_segundos, chave_para_chegada

# R4: PROXL data hora linha (Fase 1: percorre a árvore inteira)
def proximo_da_linha(arvore, data, hora, linha):
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
