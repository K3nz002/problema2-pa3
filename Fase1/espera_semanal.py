from datetime import date, timedelta
from chave import para_segundos
from proximo_da_linha import proximo_da_linha

def espera_semanal(arvore, linha, data, horario, k):
    resultado = []
    data_final = date.fromisoformat(data)
    for i in range(k - 1, -1, -1):
        dia = (data_final - timedelta(weeks=i)).isoformat()
        r = proximo_da_linha(arvore, dia, horario, linha)
        if r is None or r[0] != dia:          # não passou mais naquele dia
            resultado.append((dia, None))
        else:
            resultado.append((dia, para_segundos(r[0], r[1]) - para_segundos(dia, horario)))
    return resultado
