st1 = 'ESPERA'
st2 = 'PRONTO'
st3 = 'EXECUTANDO'
st4 = 'TERMINADO'

def removeAll(l, el):
    result = []
    for i in l:
        if i != el:
            result.append(i)
    return result


def PrimeiroAChegar(processos):
    timer = 0
    fila = []
    dicio_process = {}
    status = [0]*len(processos)
    print(dicio_process)
    for d in range(len(processos)):
        if processos[d][0] <= timer:
            if status[d] != st3:
                dicio_process[d] = [processos[d][0],processos[d][1], st2]
                status[d] = st2
        else:
            dicio_process[d] = [processos[d][0],processos[d][1], st1]
            status[d] = st1


    while True:
        for k in dicio_process.keys():
            if st3 not in status:
                if dicio_process[k][2] == st2:
                    dicio_process[k][2] = st3
                    status[k] = st3
            else:
                for j in range(len(status)):
                    if status[j] == st3:    
                        fila.append(j)
                        if fila.count(j) == dicio_process[j][1]:
                            fila = removeAll(fila, j)
                            dicio_process[j][2] = st4
                            status[j] = st4
                        break
        print(dicio_process)
        if (st2 not in status) or (0 not in status):
            break

        timer += 1
        


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