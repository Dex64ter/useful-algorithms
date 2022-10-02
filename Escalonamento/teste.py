import queue
import random

def retiraTerminado(dicio):
    for key, val in dicio.items():
        if val == "TERMINADO":
            del dicio[key]
            break

dicio = {
    1: ["TERMINADO", 1, 0],
}
# print(list(dicio.keys()))
print(dicio[1][0])
dicio[1][0] = "Executando"
print(dicio[1][0])
