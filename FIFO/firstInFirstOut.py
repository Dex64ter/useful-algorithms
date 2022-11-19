# from queue import Queue


st1 = 'ESPERA'
st2 = 'PRONTO'
st3 = 'EXECUTANDO'
st4 = 'TERMINADO'

def PrimeiroAChegar(processos):
    timer = 0
    fila = []
    dicio_process = {}
    status = []
    for d in range(len(processos)):
        dicio_process[d] = [processos[d][0],processos[d][1], st1]
        status.append(st1)
    # print(dicio_process)

    while True:
        if st3 not in status:
            for key, value in dicio_process.items():
                if dicio_process[key][2] == st1 and dicio_process[key][0] <= timer:
                    dicio_process[key][2] = st2
                    status[key] = st2
        
        timer += 1
        break


if __name__ == "__main__":
    l = []
    while True:
        try:
            entry = input()
            l.append(entry)
        except EOFError:
            break
    entrada_processos = []
    for x in l:
        entrada_processos.append(list(map(int, x.split(" "))))
    
    PrimeiroAChegar(entrada_processos)