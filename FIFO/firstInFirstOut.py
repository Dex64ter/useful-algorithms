from time import sleep

st1 = 'FORA'
st2 = 'PRONTO'
st3 = 'EXECUTANDO'
st4 = 'TERMINADO'

def verificaStatus(dicio_process):
    status = []
    for val in dicio_process.values():
        status.append(val[2])

    return status

def PrimeiroAChegar(processos):
    timer = 0
    dicio_process = {}
    tamanho = len(processos)

    for p in range(len(processos)):
            if processos[p][0] <= timer:
                dicio_process[p] = [processos[p][0],processos[p][1], st2]
            else:
                dicio_process[p] = [processos[p][0],processos[p][1], st1]

    while tamanho > 0:
        for k in dicio_process.keys():
            if dicio_process[k][2] == st3:
                timer += dicio_process[k][1]
                dicio_process.pop(k)
                tamanho -= 1
                break
            elif st3 not in verificaStatus(dicio_process):
                if dicio_process[k][2] == st2:
                    dicio_process[k][2] = st3
            elif dicio_process[k][2] == st1 and dicio_process[k][0] <= timer:
                dicio_process[k][2] = st2

            sleep(1)
        print(dicio_process, timer)
    

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