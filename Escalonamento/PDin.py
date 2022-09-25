# a. A cada processo é atribuída uma mesma prioridade de escalonamento inicial 
# que é alterada com o passar do tempo.

# b. Se o processo não está no estado executando, o escalonador periodicamente 
# aumenta a sua prioridade. 

# c. Quanto mais o processo recebe a posse da CPU mais o escalonador reduz a 
# sua prioridade.

# d. As prioridades são alteradas a cada instante de tempo.

# e. O escalonador sempre seleciona o processo com a prioridade mais alta dentre 
# aqueles no estado pronto

# f. Processos com mesma prioridade, devem seguir a ordem de chegada na fila.

# g. O escalonador DEVE forçar a preempção do processo em execução sempre 
# que houver um processo de maior prioridade

from copy import deepcopy as dpcp

st1 = 'ESPERA'
st2 = 'PRONTO'
st3 = 'EXECUTANDO'
st4 = 'TERMINADO'

def geraListaEspecifica(lis, caract):
    res = []
    for t1 in lis:
        res.append(t1[caract])
    return res


def verificaMaiorPrioridade(lis):
    ms = []
    for i in lis:
        ms.append(i[2])
    
    return ms.index(max(ms))


def PrioridadesDinamicas(entry):
    # Adição da prioridade e status:
    # 3º prioridade do processo
    # 4º status do processo
    for i in entry:
        i.append(0)
        i.append(st1)
    
    
    tempo = 0
    while True:
        for j in entry:
            if j[0] <= tempo and "EXECUTANDO" not in geraListaEspecifica(entry, 3):
                j[3] = st3
            elif j[0] <= tempo:
                j[3] = st2
            
            if j[3] == 'EXECUTANDO':
                if j[2] > 0:
                    j[2] -= 1
            else:
                j[2] += 1

        print()

        tempo += 1
        if len(set(geraListaEspecifica(entry, 3)))==1 and list(set(geraListaEspecifica(entry, 3)))[0] == "PRONTO":
            break

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
    print(entrada1)