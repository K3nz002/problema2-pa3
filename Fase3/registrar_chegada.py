from arvore_avl import *
from chave import criar_chave
from buscar_index_linha import obter_arvore_da_linha

def registrar_chegada(arvore, linhas_arvores, data, horario, linha):
    
    chave = criar_chave(data, horario, linha)
    inserido = arvore.inserir(chave)
    if inserido:
        arvore_linha = obter_arvore_da_linha(linhas_arvores, linha, nao_existe=True)
        arvore_linha.inserir(chave)
    return inserido