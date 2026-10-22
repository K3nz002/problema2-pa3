"""
A árvore guarda um único 'valor' e compara com < e ==. Cada chegada vira a
tupla (segundos, linha):
  - 'segundos' é o instante convertido em inteiro (ordem cronológica);
  - 'linha' é o texto da linha. No mesmo instante, a tupla desempata pela
    linha, comparando caractere por caractere pelo código.
Duas chegadas só são iguais se tiverem o mesmo instante e a mesma linha.
"""

from datetime import date  


def para_segundos(data, horario):
    #'2026-10-19', '18:30:00' -> inteiro que respeita a ordem cronológica.
    ano, mes, dia = data.split("-")
    h, m, s = horario.split(":")
    dias = date(int(ano), int(mes), int(dia)).toordinal()
    return dias * 86400 + int(h) * 3600 + int(m) * 60 + int(s)


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


def data_menos_dias(data, dias):
    #'2026-10-26', 7 -> '2026-10-19'
    ano, mes, dia = data.split("-")
    ordinal = date(int(ano), int(mes), int(dia)).toordinal() - dias
    return date.fromordinal(ordinal).isoformat()
