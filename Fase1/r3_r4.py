from registrar_chegada import Arvore, No


# R3: PROX data hora
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

# R4: PROXL data hora linha
def proximo_da_linha(arvore, data, hora, linha):
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

        percorrer(arvore.raiz)
        return melhor


# PROGRAMA PRINCIPAL
arvore = Arvore()

# Registros de exemplo
arvore.inserir("2026-10-22", "18:20:00", "110.2")
arvore.inserir("2026-10-22", "18:40:00", "136.1")
arvore.inserir("2026-10-22", "18:50:00", "136.1")

# R3: proxima chegada de qualquer linha
resultado = proximo(arvore, "2026-10-22", "18:30:00")

if resultado is None:
    print("NENHUM")
else:
    print(resultado.data, resultado.hora, resultado.linha)

# R4: proxima chegada de uma linha especifica
resultado = proximo_da_linha(
    "2026-10-22", "18:30:00", "136.1"
)

if resultado is None:
    print("NENHUM")
else:
    print(resultado.data, resultado.hora)
