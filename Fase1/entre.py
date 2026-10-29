from chave import para_segundos, chave_para_chegada


def entre(arvore, data1, horario1, data2, horario2):
    inicio = para_segundos(data1, horario1)
    fim = para_segundos(data2, horario2)
    resultado = []
    if inicio > fim:
        return resultado

    pilha = []
    atual = arvore.raiz
    while True:
        while atual is not None:
            if atual.valor[0] >= inicio:     # valor[0] = segundos da chegada
                pilha.append(atual)          # pode haver itens à esquerda
                atual = atual.esq
            else:                            # nó e subárvore esquerda: antes do início
                atual = atual.dir
        if not pilha:
            break
        no = pilha.pop()
        if no.valor[0] > fim:                # tudo dali em diante é maior
            break
        resultado.append(chave_para_chegada(no.valor))
        atual = no.dir
    return resultado
