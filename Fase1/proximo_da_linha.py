from busca_binaria import Arvore, No


# R4: PROXL data hora linha
def proximo_da_linha(arvore, data, hora, linha):
    melhor = None
    instante = (data, hora)

    def percorrer(no):
        nonlocal melhor

        if no is None:
            return

        instante_atual = (no.data, no.hora)

        if no.linha == linha and instante_atual >= instante:
            if melhor is None or instante_atual < (
                melhor.data, melhor.hora
            ):
                melhor = no

        percorrer(no.esq)
        percorrer(no.dir)

    percorrer(arvore.raiz)
    return melhor
