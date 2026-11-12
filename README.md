# Problema 2 – A que horas passa o próximo ônibus?

## Requisitos
- Python 3.13 (testado com 3.13.15), sem bibliotecas externas.
- Comandos executados no Windows, a partir da raiz do repositório.

## Como executar
Os comandos de compilação e execução de cada fase estão em `executar.txt`.

Fase 1 (árvore binária de busca):
```
python Fase1/main.py "Arquivos P2/pequeno.txt"
```
As respostas saem na saída padrão; o tempo das operações sai na saída de erro, como `TEMPO_MS valor`.

Conferir com a resposta esperada (PowerShell):
```
python Fase1/main.py "Arquivos P2/pequeno.txt" > saida.txt
Compare-Object (Get-Content saida.txt) (Get-Content "Arquivos P2/pequeno_esperado_fase1.txt")
```

## Fase 2 (medições)
Executa cada arquivo de carga 5 vezes com a árvore da Fase 1 e gera a tabela com a mediana dos tempos, a altura final e o pico de memória:
```
python Fase2/medir.py
```
A tabela é impressa na tela e salva em `Fase2/resultados_Fase1.md`.

O pico de memória é medido com `tracemalloc` (biblioteca padrão) em uma execução extra de cada arquivo, separada das 5 cronometradas, porque o `tracemalloc` deixa o programa mais lento. Para isso o `medir.py` define a variável de ambiente `MEDIR_MEMORIA=1`, e o `main.py` passa a escrever `MEMORIA_KB valor` na saída de erro. Sem essa variável, o `main.py` funciona normalmente, sem medir memória.

## Fase 3 (árvore AVL)
Executar:
```
python Fase3/main.py "Arquivos P2/pequeno.txt"
```

Conferir com a resposta esperada (PowerShell):
```
python Fase3/main.py "Arquivos P2/pequeno.txt" > saida.txt
Compare-Object (Get-Content saida.txt) (Get-Content "Arquivos P2/pequeno_esperado_fase3.txt")
```

Medições com os mesmos arquivos de carga da Fase 2 (5 execuções por arquivo, mediana dos tempos, altura final e pico de memória):
```
python Fase2/medir.py Fase3/main.py
```
A tabela é impressa na tela e salva em `Fase2/resultados_Fase3.md`. A comparação lado a lado com a Fase 1 usa `Fase2/resultados_Fase1.md` e `Fase2/resultados_Fase3.md`, gerados na mesma máquina.

## Uso de IA
- Testes do código afim de identificar erros com o Gemini IA
- Pesquisa sobre a estrutura de árvore binária com Perplexity
- Correção de integração entre os módulos da F, com auxílio do Gemini IA Fase 1 (chave única, retornos e R8)
- Pesquisa sobre árvores AVL com Perplexity
- Resumo da fonte https://docs.python.org/3/library/tracemalloc.html sintetizando o método de funcionamento com Claude AI
