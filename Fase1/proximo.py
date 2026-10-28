from busca_binaria import Arvore, No

def proximo(arvore, data, hora):
    atual = arvore.raiz
    melhor = None
    instante = (data, hora)

    while atual is not None:
        instante_atual = (atual.data, atual.hora)

        if instante_atual >= instante:
            melhor = atual
            atual = atual.esq
        else:
            atual = atual.dir

    return melhor
