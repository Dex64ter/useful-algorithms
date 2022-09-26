from copy import deepcopy as dpcp
from time import sleep

st1 = 'ESPERA'
st2 = 'PRONTO'
st3 = 'EXECUTANDO'
st4 = 'TERMINADO'

# Gera lista de uma determinada característica do processo
def geraListaEspecifica(lis, caract):
    res = []
    for t1 in lis:
        res.append(t1[caract])
    return res

# verifica o processo com maior prioridade que esteja no estado pronto
# caso não tenha nenhum pronto, devolve -1
def verificaMaiorPrioridade(lis):
    ms = [-1]*len(lis)
    for i in range(len(lis)):
        if lis[i][3] == st2:
            ms[i] = (lis[i][2])
    
    if max(ms) != -1:
        return ms.index(max(ms))
    else:
        return -1

# função principal das Prioridades Dinâmicas
def PrioridadesDinamicas(entry):
    # Listas para somatório e transformação dos resultados
    tempRetorno = [0]*len(entry)
    tempResposta = [0]*len(entry)
    tempEspera = [0]*len(entry)

    # Adição da prioridade e status:
    # 3º prioridade do processo
    # 4º status do processo
    for i in entry:
        i.append(0)
        i.append(st1)
    
    finished = [0]*len(entry)       # lista para decidir se um processo já executou no número adequado de vezes
    tempo = 0           # tempo do processamento
    while True:
        if st3 in geraListaEspecifica(entry, 3):            # Parte que verifica quando um processo já está em execução
            k1 = geraListaEspecifica(entry, 3).index(st3)   # e verifica qual processo está em execução
            finished[k1] += 1                               # adicionando o tempo de processo dele
            if verificaMaiorPrioridade(entry) != -1 :
                k2 = verificaMaiorPrioridade(entry)         # verifica qual o processo está com maior prioridade naquele momento
                if k1 != k2:
                    if entry[k1][1] == finished[k1]:            
                        entry[k1][3], entry[k2][3] = st4 , st3  # coloca o processo com maior prioridade em execução
                        entry[k1][2] = -1                       # caso o processo anterior tenha acabado o seu tempo de execução ele entra em estado "TERMINADO"
                    else:
                        entry[k1][3], entry[k2][3] = st2 , st3  # senão volta pro estado pronto
                    
                    if finished[k2] == 0:
                        tempResposta[k2] = tempo - entry[k2][0] # Calculo do tempo de resposta de cada processo

            tempRetorno[k1] = tempo - entry[k1][0]              # calcilo do tempo de Retorno de cada processo
            
        for j in range(len(entry)):             # loop para verificar o estado de cada processo
            
            if entry[j][3] == st4:
                continue
            elif entry[j][3] == st3 and finished[j] == entry[j][1]:
                entry[j][3] = st4
            elif (entry[j][0] <= tempo) and (st3 not in geraListaEspecifica(entry, 3)) and entry[j][3] != st4:
                entry[j][3] = st3
                tempResposta[j] = tempo - entry[j][0]
            elif entry[j][0] <= tempo and entry[j][3] == st1:
                entry[j][3] = st2

            if entry[j][3] == st3:
                if entry[j][2] > 0:
                    entry[j][2] -= 1
            elif entry[j][3] == st4:
                continue
            else:
                entry[j][2] += 1

            if entry[j][3] == st2:
                tempEspera[j] += 1
        tempo += 1
        if len(set(geraListaEspecifica(entry, 3)))==1 and list(set(geraListaEspecifica(entry, 3)))[0] == st4:       # verifica se todos os processos já terminaram
            break
    print("PRI %.2f %.2f %.2f" % (sum(tempRetorno)/len(entry), sum(tempResposta)/len(entry), sum(tempEspera)/len(entry))) # manipulação do resultados para prioridades dinâmicas
    

# Função de processamento da entrada
# recebimento por leitura de arquivo e
# formatação para uma lista de listas
def procesEntry(into):
    s=[]
    for i in into:
        s.append(list(map(int, i.split(" "))))
    return s


if __name__ == "__main__":
    
    with open('file.txt', 'r+') as entry:
        entrada = entry.read()
        entrada = entrada.split("\n")

    # Entrada de dados:
    # 1º - instante da chegada do processo;
    # 2º - duração de cada processo
    entrada0 = procesEntry(entrada)
    entrada1 = dpcp(entrada0)
    entrada2 = dpcp(entrada0)

    PrioridadesDinamicas(entrada1)
    