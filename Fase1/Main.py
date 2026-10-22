import sys
import threading
import time

from arvore import Arvore
from r1_registrar_chegada import registrar_chegada
from r2_buscar_chegada import buscar_chegada
from r3_proximo import proximo
from r4_proximo_da_linha import proximo_da_linha
from r5_entre import entre
from r6_remover_chegada import remover_chegada
from r7_altura import altura
from r8_espera_semanal import espera_semanal


def ler_operacoes(caminho):
    operacoes = []
    with open(caminho, "r", encoding="utf-8") as arq:
        for linha in arq:
            texto = linha.strip()
            if texto == "" or texto.startswith("#"):
                continue
            operacoes.append(texto.split())
    return operacoes


def executar(arvore, op, saida):
    cmd = op[0]

    if cmd == "REG":                                        # R1
        ok = registrar_chegada(arvore, op[1], op[2], op[3])
        saida.append("OK" if ok else "DUPLICADO")

    elif cmd == "BUSCA":                                    # R2
        achou = buscar_chegada(arvore, op[1], op[2], op[3])
        saida.append("ACHOU" if achou else "NAO")

    elif cmd == "PROX":                                     # R3
        r = proximo(arvore, op[1], op[2])
        saida.append("NENHUM" if r is None else "%s %s %s" % r)

    elif cmd == "PROXL":                                    # R4
        r = proximo_da_linha(arvore, op[1], op[2], op[3])
        saida.append("NENHUM" if r is None else "%s %s" % r)

    elif cmd == "ENTRE":                                    # R5
        lista = entre(arvore, op[1], op[2], op[3], op[4])
        saida.append(str(len(lista)))
        for item in lista:
            saida.append("%s %s %s" % item)

    elif cmd == "REM":                                      # R6
        ok = remover_chegada(arvore, op[1], op[2], op[3])
        saida.append("OK" if ok else "NAO")

    elif cmd == "ALT":                                      # R7
        saida.append(str(altura(arvore)))

    elif cmd == "SEMANA":                                   # R8
        lista = espera_semanal(arvore, op[1], op[2], op[3], int(op[4]))
        for data_i, espera in lista:
            saida.append("%s %s" % (data_i, "NAOPASSOU" if espera is None else espera))


def rodar(caminho):
    operacoes = ler_operacoes(caminho)        # lê tudo antes de executar
    arvore = Arvore()
    saida = []

    inicio = time.perf_counter()              # mede as operações
    for op in operacoes:
        executar(arvore, op, saida)
    fim = time.perf_counter()

    if saida:
        sys.stdout.write("\n".join(saida) + "\n")
    sys.stderr.write("TEMPO_MS %.3f\n" % ((fim - inicio) * 1000))


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Uso: python sistema.py arquivo_de_operacoes.txt\n")
        return

    sys.setrecursionlimit(1000000)
    threading.stack_size(256 * 1024 * 1024)
    t = threading.Thread(target=rodar, args=(sys.argv[1],))
    t.start()
    t.join()


if __name__ == "__main__":
    main()
