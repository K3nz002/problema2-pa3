"""
A árvore guarda um único 'valor' e compara com < e ==. Cada chegada vira a
tupla (segundos, linha):
  - 'segundos' é o instante convertido em inteiro (ordem cronológica);
  - 'linha' é o texto da linha. No mesmo instante, a tupla desempata pela
    linha, comparando caractere por caractere pelo código.
Duas chegadas só são iguais se tiverem o mesmo instante e a mesma linha.
"""

from datetime import date, timedelta

def para_segundos(data_str, horario_str):
    ano, mes, dia = map(int, data_str.split("-"))
    h, m, s = map(int, horario_str.split(":"))

    data = date(ano, mes, dia)
    segundos_do_dia = h * 3600 + m * 60 + s
    return data.toordinal() * 86400 + segundos_do_dia

def criar_chave(data, horario, linha):
    #(data, horario, linha) -> valor que vai dentro da árvore.
    return (para_segundos(data, horario), linha)


def chave_para_chegada(chave):
    """Valor da árvore -> (data, horario, linha), no formato do arquivo."""
    seg, linha = chave
    data = date.fromordinal(seg // 86400).isoformat()
    resto = seg % 86400
    horario = "%02d:%02d:%02d" % (resto // 3600, resto % 3600 // 60, resto % 60)
    return (data, horario, linha)
