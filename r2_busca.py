def buscar_chegada(arvore, data, horario, linha):
valor = (data, horario, linha)
resultado = arvore.buscar(valor)

if resultado:
return "ACHOU"
else:
return "NAO"
