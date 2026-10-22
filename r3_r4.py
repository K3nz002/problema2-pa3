class No:
    def __init__(self, data, hora, linha):
        self.data = data
        self.hora = hora
        self.linha = linha
        self.esq = None
        self.dir = None


class Arvore:
    def __init__(self):
        self.raiz = None

    # Inserir registro na arvore
    def inserir(self, data, hora, linha):
        novo = No(data, hora, linha)
        chave_nova = (data, hora, linha)

        if self.raiz is None:
            self.raiz = novo
            return True

        atual = self.raiz

        while True:
            chave_atual = (
                atual.data,
                atual.hora,
                atual.linha
            )

            if chave_nova == chave_atual:
                return False

            if chave_nova < chave_atual:
                if atual.esq is None:
                    atual.esq = novo
                    return True
                atual = atual.esq
            else:
                if atual.dir is None:
                    atual.dir = novo
                    return True
                atual = atual.dir

    # R3: PROX data hora
    def proximo(self, data, hora):
        atual = self.raiz
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

    # R4: PROXL data hora linha
    def proximo_da_linha(self, data, hora, linha):
        melhor = None

        def percorrer(no):
            nonlocal melhor

            if no is None:
                return

            instante = (no.data, no.hora)

            if no.linha == linha and instante >= (data, hora):
                if melhor is None or instante < (
                    melhor.data, melhor.hora
                ):
                    melhor = no

            percorrer(no.esq)
            percorrer(no.dir)

        percorrer(self.raiz)
        return melhor


# PROGRAMA PRINCIPAL
arvore = Arvore()

# Registros de exemplo
arvore.inserir("2026-10-22", "18:20:00", "110.2")
arvore.inserir("2026-10-22", "18:40:00", "136.1")
arvore.inserir("2026-10-22", "18:50:00", "136.1")

# R3: proxima chegada de qualquer linha
resultado = arvore.proximo("2026-10-22", "18:30:00")

if resultado is None:
    print("NENHUM")
else:
    print(resultado.data, resultado.hora, resultado.linha)

# R4: proxima chegada de uma linha especifica
resultado = arvore.proximo_da_linha(
    "2026-10-22", "18:30:00", "136.1"
)

if resultado is None:
    print("NENHUM")
else:
    print(resultado.data, resultado.hora)
