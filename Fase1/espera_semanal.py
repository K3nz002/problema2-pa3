from datetime import datetime, timedelta
from buscar_chegada

def espera_semanal(linha, data, horario, k):
    data_final = datetime.strptime(data, '%Y-%m-%d')
    horario_esperado = datetime.strptime(horario, '%H:%M:%S').time()
    # De i = k - 1 até 0 (da semana mais antiga até a data informada)
    for i in range(k - 1, -1, -1):
        data_atual = data_final - timedelta(weeks=i)
        data_atual_str = data_atual.strftime('%Y-%m-%d')
        chegadas = buscar_chegada(data_atual_str, horario, linha)
        horario_chegada = None
        
        for chegada in chegadas:
            if chegada.hora >= horario_esperado:
                horario_chegada = chegada.horario
                break

        if horario_chegada is not None:
            horario_esperado = datetime.strptime(f"{data_atual_str} {horario}", '%Y-%m-%d %H:%M:%S')
            horario_chegada = datetime.strptime(f"{data_atual_str} {horario_chegada}", '%Y-%m-%d %H:%M:%S')
            segundos_espera = int((horario_chegada - horario_esperado).total_seconds())
            print(f"{data_atual_str} {segundos_espera}")
        else:
            print(f"{data_atual_str} NAOPASSOU")