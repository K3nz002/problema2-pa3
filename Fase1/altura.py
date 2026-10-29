def altura(no):
    if no is None:
        return 0

    altura_esq = altura(no.esq)
    altura_dir = altura(no.dir)

    return 1 + max(altura_esq, altura_dir)