"""
Fase 2: mede a árvore da Fase 1 com os arquivos de carga.

Roda cada arquivo de carga REPETICOES vezes, com um ALT acrescentado no fim
para obter a altura final, e monta a tabela com a mediana dos tempos.
Script de medição (fora do núcleo): pode usar estruturas prontas.

Uso, a partir da raiz do repositório:
    python Fase2/medir.py                      # mede Fase1/main.py, 5 vezes
    python Fase2/medir.py Fase3/main.py 5      # mesma medição para a Fase 3
"""

import os
import statistics
import subprocess
import sys
import tempfile

PASTA_CARGA = "Arquivos P2"
VERSOES = ["quase_ordem", "embaralhada"]
TAMANHOS = [1000, 5000, 20000]


def executar_uma_vez(programa, arquivo):
    proc = subprocess.run([sys.executable, programa, arquivo],
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError("falha ao executar %s:\n%s" % (arquivo, proc.stderr))
    tempo = None
    for linha in proc.stderr.splitlines():
        if linha.startswith("TEMPO_MS"):
            tempo = float(linha.split()[1])
    altura = int(proc.stdout.strip().splitlines()[-1])   # resposta do ALT final
    return tempo, altura


def medir(programa, versao, n, repeticoes):
    origem = os.path.join(PASTA_CARGA, "carga_%s_%d.txt" % (versao, n))
    with open(origem, "r", encoding="utf-8") as arq:
        conteudo = arq.read()

    # cópia temporária da carga com ALT no final
    fd, temporario = tempfile.mkstemp(suffix=".txt")
    with os.fdopen(fd, "w", encoding="utf-8") as arq:
        arq.write(conteudo.rstrip("\n") + "\nALT\n")

    try:
        tempos = []
        altura = None
        for i in range(repeticoes):
            tempo, altura = executar_uma_vez(programa, temporario)
            tempos.append(tempo)
            sys.stderr.write("  %s N=%d execução %d/%d: %.3f ms\n"
                             % (versao, n, i + 1, repeticoes, tempo))
    finally:
        os.remove(temporario)

    return statistics.median(tempos), altura, tempos


def main():
    programa = sys.argv[1] if len(sys.argv) > 1 else "Fase1/main.py"
    repeticoes = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    resultados = {}
    for versao in VERSOES:
        for n in TAMANHOS:
            resultados[(versao, n)] = medir(programa, versao, n, repeticoes)

    linhas = []
    linhas.append("Programa: %s | repetições por arquivo: %d | Python %s"
                  % (programa, repeticoes, sys.version.split()[0]))
    linhas.append("")
    linhas.append("| Versão | N | Mediana (ms) | Altura final | Tempos (ms) |")
    linhas.append("|---|---|---|---|---|")
    for versao in VERSOES:
        for n in TAMANHOS:
            mediana, altura, tempos = resultados[(versao, n)]
            linhas.append("| %s | %d | %.3f | %d | %s |" % (
                versao, n, mediana, altura,
                ", ".join("%.3f" % t for t in tempos)))
    linhas.append("")
    linhas.append("Razão T(N=20000) / T(N=1000):")
    for versao in VERSOES:
        razao = resultados[(versao, 20000)][0] / resultados[(versao, 1000)][0]
        linhas.append("- %s: %.1f" % (versao, razao))

    texto = "\n".join(linhas) + "\n"
    sys.stdout.write(texto)

    pasta = os.path.dirname(os.path.abspath(__file__))
    nome = "resultados_%s.md" % os.path.basename(os.path.dirname(os.path.abspath(programa)))
    with open(os.path.join(pasta, nome), "w", encoding="utf-8") as arq:
        arq.write(texto)
    sys.stderr.write("Tabela salva em %s\n" % os.path.join("Fase2", nome))


if __name__ == "__main__":
    main()
