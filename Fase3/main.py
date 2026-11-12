import os
import sys
import threading
import time
import tracemalloc
from arvore_avl import *
from registrar_chegada import registrar_chegada
from buscar_chegada import buscar_chegada
from buscar_index_linha import *
from proximo import proximo
from proximo_da_linha import proximo_da_linha
from entre import entre
from remover_chegada import remover_chegada
from altura import altura
from espera_semanal import espera_semanal


def ler_operacoes(caminho):
    operacoes = []
    with open(caminho, "r", encoding="utf-8-sig") as arq:
        for linha in arq:
            texto = linha.strip()
            if texto == "" or texto.startswith("#"):
                continue
            operacoes.append(texto.split())
    return operacoes


def executar(arvore, linhas_arvores, op, saida):
    cmd = op[0]

    if cmd == "REG":                                        # R1
        ok = registrar_chegada(arvore, linhas_arvores, op[1], op[2], op[3])
        saida.append("OK" if ok else "DUPLICADO")

    elif cmd == "BUSCA":                                    # R2
        achou = buscar_chegada(arvore, op[1], op[2], op[3])
        saida.append("ACHOU" if achou else "NAO")

    elif cmd == "PROX":                                     # R3
        r = proximo(arvore, op[1], op[2])
        saida.append("NENHUM" if r is None else "%s %s %s" % r)

    elif cmd == "PROXL":                                    # R4
        r = proximo_da_linha(linhas_arvores, op[1], op[2], op[3])
        saida.append("NENHUM" if r is None else "%s %s" % r)

    elif cmd == "ENTRE":                                    # R5
        lista = entre(arvore, op[1], op[2], op[3], op[4])
        saida.append(str(len(lista)))
        for item in lista:
            saida.append("%s %s %s" % item)

    elif cmd == "REM":                                      # R6
        ok = remover_chegada(arvore, linhas_arvores, op[1], op[2], op[3])
        saida.append("OK" if ok else "NAO")

    elif cmd == "ALT":                                      # R7
        saida.append(str(altura(arvore.raiz)))

    elif cmd == "SEMANA":                                   # R8
        lista = espera_semanal(linhas_arvores, op[1], op[2], op[3], int(op[4]))
        for data_i, espera in lista:
            saida.append("%s %s" % (data_i, "NAOPASSOU" if espera is None else espera))
    elif cmd == "LINHAS":
        lista = entre(arvore, op[1], op[2], op[3], op[4])
        saida.append(str(len(lista)))
        for item in lista:
            saida.append("%s %s %s" % item)


def rodar(caminho):
    operacoes = ler_operacoes(caminho)        # lê tudo antes de executar
    arvore = Arvore()
    linhas_arvores = []
    saida = []

    medir_memoria = os.environ.get("MEDIR_MEMORIA") == "1"
    if medir_memoria:
        tracemalloc.start()

    inicio = time.perf_counter()              # mede as operações
    for op in operacoes:
        executar(arvore, linhas_arvores, op, saida)
    fim = time.perf_counter()

    if medir_memoria:
        _, pico = tracemalloc.get_traced_memory()
        tracemalloc.stop()

    if saida:
        sys.stdout.write("\n".join(saida) + "\n")
    sys.stderr.write("TEMPO_MS %.3f\n" % ((fim - inicio) * 1000))
    if medir_memoria:
        sys.stderr.write("MEMORIA_KB %.1f\n" % (pico / 1024))


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Uso: python Fase3/main.py arquivo_de_operacoes.txt\n")
        return

    sys.setrecursionlimit(1000000)
    try:    
        threading.stack_size(64 * 1024 * 1024)
    except (ValueError, OverflowError):
        pass
    t = threading.Thread(target=rodar, args=(sys.argv[1],))
    t.start()
    t.join()


if __name__ == "__main__":
    main()
