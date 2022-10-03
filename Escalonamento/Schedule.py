from random import choice
from time import sleep

quantum = 2
st1 = 'ESPERA'
st2 = 'PRONTO'
st3 = 'EXECUTANDO'
st4 = 'TERMINADO'

# usado em Loteria
def trocaExecucao(dicio):
    for key, val in dicio.items():
        if val == st3:
            return key
    return -1

def maiorProcesso(dicio):
    for key, val in dicio.items():
        if val == max(dicio.values()):
            return key

# função principal das Prioridades Dinâmicas
def prioridadesDinamicas(entry):
    tempRetorno = [0]*len(entry)
    tempResposta = [0]*len(entry)
    tempEspera = [0]*len(entry)
    dicio_process = {}
    timer = 0
    lista_execucoes = []
    for i in range(len(entry)):
        dicio_process[i] = [st1, 0, entry[i][1]]
    
    while dicio_process:
        laux1={}
        laux2={}
        for n in dicio_process.keys():
            if dicio_process[n][0] != st3:
                if entry[n][0] <= timer:
                    dicio_process[n][0] = st2
            laux1[n] = (dicio_process[n][0])
            laux2[n] = (dicio_process[n][1])
        
        prontos = {}
        for kk , vv in dicio_process.items():
            if vv[0] != st1:
                prontos[kk] = vv

        if dicio_process:
            if st3 in laux1.values():
                proc_atual = -1
                for key, val in dicio_process.items():
                    if val[0] == st3:
                        proc_atual = key
                        if dicio_process[key][1] > 0:
                            dicio_process[key][1] -= 1
                        laux2[key] = dicio_process[key][1]
                    else:
                        dicio_process[key][1] += 1
                        laux2[key] = dicio_process[key][1]

                for k, v in laux2.items():
                    if v == max(laux2.values()):
                        if k != proc_atual and laux1[k] == st2:                            
                                dicio_process[proc_atual][0] = st2 
                                dicio_process[k][0] = st3
                                if k not in lista_execucoes:
                                    tempResposta[k] = timer - entry[k][0]
                                lista_execucoes.append(proc_atual)
                                break
                        elif k != proc_atual:
                            kaux = maiorProcesso(prontos)
                            dicio_process[proc_atual][0] = st2
                            dicio_process[kaux][0] = st3
                            if kaux not in lista_execucoes:
                                    tempResposta[k] = timer - entry[k][0]
                            lista_execucoes.append(proc_atual)
                            break
                        else:
                            lista_execucoes.append(k)
            else:
                if st2 in laux1.values():
                    for key, val in dicio_process.items():
                        if val[1] == max(laux2.values()):
                            if dicio_process[key][0] == st2:
                                if key not in lista_execucoes:
                                    tempResposta[key] = timer - entry[key][0]
                                dicio_process[key][0] = st3
                                break
                    
                    for key, val in dicio_process.items():
                        if val[0] == st3:
                            if dicio_process[key][1] > 0:
                                dicio_process[key][1] -= 1
                        else:
                            dicio_process[key][1] += 1

        remv = -1
        for i in list(set(lista_execucoes)):
            if lista_execucoes.count(i) == dicio_process[i][2]:
                remv = i
                tempRetorno[i] = timer - entry[i][0]
                del dicio_process[i]

        if remv != -1:
            lista_execucoes = list(filter(lambda val: val != remv, lista_execucoes))

        for z, x in dicio_process.items():
            if x[0] == st2:
                tempEspera[z] += 1
        print(dicio_process)
        sleep(1.5)
        timer += 1
    print("PRI %.2f %.2f %.2f" % (sum(tempRetorno)/len(entry), sum(tempResposta)/len(entry), sum(tempEspera)/len(entry))) # manipulação do resultados para prioridades dinâmicas
    


def loteria(entry):
    tempRetorno = [0]*len(entry)
    tempResposta = [0]*len(entry)
    tempEspera = [0]*len(entry)
    process_dicio = {}
    tempo = 0
    lista_execucao = []
    for i in range(len(entry)):
        process_dicio[i] = st1
    
    while True:
        remv = -1
        for x in process_dicio.keys():
            if (lista_execucao.count(x)*quantum) >= entry[x][1]:
                remv = x
            elif process_dicio[x] != st3:
                if (entry[x][0]) <= tempo:
                    if process_dicio[x] == st1:
                        tempRetorno[x] = tempo
                        tempResposta[x] = tempo
                    process_dicio[x] = st2
                    tempEspera[x] += 1

        if remv != -1:
            del process_dicio[remv]
            tempRetorno[remv] = tempo - tempRetorno[remv]
            lista_execucao = list(filter(lambda val: val != remv, lista_execucao))
        # print(process_dicio, " - ", tempRetorno)
        if process_dicio:
            dicio_prontos_exec = {}
            for k, v in process_dicio.items():
                if v != st1:
                    dicio_prontos_exec[k] = v

            if dicio_prontos_exec:
                proc = choice(list(dicio_prontos_exec.keys()))
                troca = trocaExecucao(dicio_prontos_exec)
                if troca == -1:
                    process_dicio[proc] = st3
                    if proc not in lista_execucao:
                        tempResposta[proc] = tempo - tempResposta[proc] 
                else:
                    process_dicio[troca] = st2
                    lista_execucao.append(troca)
                    process_dicio[proc] = st3
                    if proc not in lista_execucao:
                        tempResposta[proc] = tempo - tempResposta[proc]
        else:
            break
        tempo += quantum
    print("LOT %.2f %.2f %.2f" % (sum(tempRetorno)/len(entry), sum(tempResposta)/len(entry), sum(tempEspera)/len(entry)))
    
def roundRobin(entry):
    dicio_process = {}
    tempEspera = [0]*len(entry)
    tempResposta = [-1]*len(entry)
    tempRetorno = [0]*len(entry)
    comeco_fila = 0
    timer = 0
    for i in range(len(entry)):
        dicio_process[i] = entry[i][1]
    
    while dicio_process:
        if comeco_fila == len(entry):
            comeco_fila = 0
        # print(dicio_process, timer, "== ", tempEspera)
        
        if comeco_fila in dicio_process.keys():
            if entry[comeco_fila][0] <= timer:
                aux = False
                va = 0
                dicio_process[comeco_fila] = dicio_process[comeco_fila] - quantum
                if tempResposta[comeco_fila] == -1:
                    tempResposta[comeco_fila] = timer - entry[comeco_fila][0]
                if dicio_process[comeco_fila] <= 0:
                    aux = True
                    va = dicio_process[comeco_fila]
                    timer += dicio_process[comeco_fila] + quantum
                    tempRetorno[comeco_fila] = timer - entry[comeco_fila][0]
                    del dicio_process[comeco_fila]
                else:
                    timer += quantum

                for i in dicio_process.keys():
                    if i != comeco_fila:
                        if not aux:
                            tempEspera[i] += quantum
                        else:
                            tempEspera[i] += va + quantum

            else:
                timer += quantum
            comeco_fila += 1
        else:
            comeco_fila += 1
    for j in range(len(tempEspera)):
        tempEspera[j] = tempEspera[j] - entry[j][0]
    print("RR %.2f %.2f %.2f" % (sum(tempRetorno)/len(entry), sum(tempResposta)/len(entry), sum(tempEspera)/len(entry)))


if __name__ == "__main__":
    l = []
    while True:
        try:
            e = input()
            l.append(e)
        except EOFError:
            break

    entrada = []
    for i in l:
        entrada.append(list(map(int, (i.strip()).split(" "))))
    # print(entrada)
    prioridadesDinamicas(entrada)
    loteria(entrada)
    roundRobin(entrada)
