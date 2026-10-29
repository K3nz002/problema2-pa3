from chave import para_segundos, chave_para_chegada

def proximo(arvore, data, hora):
    atual = arvore.raiz
    melhor = None
    instante = para_segundos(data, hora)
    while atual is not None:
        if atual.valor[0] >= instante:
            melhor = atual
            atual = atual.esq
        else:
            atual = atual.dir
    return None if melhor is None else chave_para_chegada(melhor.valor)
