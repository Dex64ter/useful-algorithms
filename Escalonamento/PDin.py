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


def Prioridades(entry):
    # Adição da prioridade e status:
    # 3º prioridade do processo
    # 4º status do processo
    for i in entry:
        i.append(0)
        i.append(st1)
    
    lista_auxiliar = [st1]*len(entry)
    tempo = 0
    while entry:
        for j in entry:
            if j[0] <= tempo:
                if j[3] == st1:
                    j[3] = st2
                    if st3 not in lista_auxiliar:
                        j[3] = st3
                elif j[3] == st3:
                    if j[2] > 0:
                        j[2] -= 1
                else:
                    j[2] += 1



            j[2] += 1
        tempo += 1

# Função de processamento da entrada
# recebimento por leitura de arquivo e
# formatação para uma lista de listas
def procesEntry(into):
    s=[]
    for i in into:
        s.append(i.split(" "))
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

    Prioridades(entrada1)