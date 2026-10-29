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
Executa cada arquivo de carga 5 vezes com a árvore da Fase 1 e gera a tabela com a mediana dos tempos e a altura final:
```
python Fase2/medir.py
```
A tabela é impressa na tela e salva em `Fase2/resultados_Fase1.md`.

## Uso de IA
- Testes do código afim de identificar erros
- Pesquisa sobre a estrutura de árvore binária
- Correção de integração entre os módulos da Fase 1 (chave única, retornos e R8)
