from arvore_avl import Arvore
def buscar_indice_linha(linhas_arvores, nome_linha):
    """Busca binária na lista de pares [nome_linha, arvore]."""
    ini = 0
    fim = len(linhas_arvores) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if linhas_arvores[meio][0] == nome_linha:
            return True, meio
        elif linhas_arvores[meio][0] < nome_linha:
            ini = meio + 1
        else:
            fim = meio - 1
    return False, ini

def obter_arvore_da_linha(linhas_arvores, nome_linha, nao_existe=True):
    achou, idx = buscar_indice_linha(linhas_arvores, nome_linha)
    if achou:
        return linhas_arvores[idx][1]
    if nao_existe:
        nova_arvore = Arvore()
        linhas_arvores.insert(idx, [nome_linha, nova_arvore])
        return nova_arvore
    return None