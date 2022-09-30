from queue import Queue
from time import sleep

# Lista de referências, index da referência a ser verificada, dicionário sendo utilizado
# função que auxilia nos dicionários criados para referenciar os rotulos das referências à memória
# Ele verifica se um elemento ainda será usado no decorrer da entrada ou não, e em qual posição está a próxima referência
# Atualizando a posição da próxima referência no dicionário 
def attDicio(entry, index, dicio):
    if entry[index] in entry[index+1:]:
        dicio[entry[index]] = entry[index+1:].index(entry[index])+(index+1)
    else:
        dicio[entry[index]] = -1

# Função que verifica se a página dentro do slot ainda vai ser utilizada futuramente ou se já
# não vai mais ser usada, caso ela n seja mais usada, ela devolve -1 e ela será a substituída
# caso todas ainda sejam usadas, ele devolve a com maior rótulo (posição mais distnate a ser executada)
# para ser substituída 
def pegaMaiorRotulo( dicio):
    if -1 not in dicio.values():
        for key, value in dicio.items():
            if value == max(dicio.values()):
                return key

    else:
        for key, value in dicio.items():
            if value == -1:
                return key



def conjuntoTrabalho(slots, entry):         # OK
    page_faults = 0
    limiar = int(slots/2) + 1
    ws = set()
    pages = set()
    
    for i in range(len(entry)):             # loop para todas as referências
        if len(ws) < limiar:                # parte da funçaõ que verifica quais referências vão estar no cnjunto de trabalho
            if entry[i] not in ws:          # se a referência não estiver no conjunto de trabalho ele entra
                ws.add(entry[i])
        else:
            ws = set(entry[i-limiar:i])     # caso o conjunto de trabalho estiver cheio, ele atualiza o conjunto de trabalho com os últimos processos mantendo o tamanho do limiar
            
        if len(pages) < slots:              # Caso os slots estiverem vazios
            if entry[i] not in pages:       # E a referência não já estiver nos slots, adiciona o processo nos slots vazios
                pages.add(entry[i])
                page_faults += 1            # Adiciona falta de páginas a todos que foram adicionados
        else:
            if entry[i] not in pages:                       # caso os slots estejam cheios
                pages.remove(list(pages.difference(ws))[0]) # Verifica quais dos processos não está no working set
                pages.add(entry[i])                         # e substitui o que não está no working set 
                page_faults += 1

    print("CT", page_faults)


def algOtimo(slots, entry):                 # OK
    page_faults = 0                     # contagem de falta de páginas
    pages = set()                       # slots da memória
    pag = {}                            # Dicionário para o auxílio da definição dos rótulos

    for i in range(len(entry)):         
        if len(pages) < slots:          # com os slots vazios e sem repetição de referência
            if entry[i] not in pages:   
                pages.add(entry[i])     # as referências vão sendo alocadas
                page_faults += 1        # junto com o acréscimo nas faltas de páginas
                attDicio(entry, i, pag) # E adiciona o elemeno no dicionário
        else:
            if entry[i] not in pages:       # Aqui faz a verificação se a referência não está nos slots 
                page_faults += 1   
                r = pegaMaiorRotulo(pag) 
                pages.remove(r)  # verifica qual a com maior rótulo ou se tem alguma que já acabou seu uso
                del pag[r]
                pages.add(entry[i])                 # atualiza os slots
                attDicio(entry, i, pag)             # atualiza o dicionário
            else:
                attDicio(entry, i, pag)             # caso ele já esteja nos slots apenas atualiza os rótulos
        # print(pages, pag)
        # sleep(2)
    print("OTM %d" % (page_faults))

# Função para imprimir o resultado do algoritmo de segunda chance
def secondChance(slots, entry):                 # OK
    falta_pag = 0           # contador da faltas de página com o algoritmo
    lista_auxiliar = []     # lista que ajudará na contagem das referências a memória de cada processo
    pages = set()           # cria-se um set para significar os espaços na memória física
    lugares = Queue()       # e um objeto fila para identificar os processos que já estão a muito tempo nela
    
    for i in range(len(entry)): # loop pelas referências
        # Enquanto os slots não estiverem cheios
        # ele adiciona as referências aos slots junto ao acréscimo das faltas de páginas e entrada na fila 
        if len(pages) < slots: 
            if entry[i] not in pages:
                pages.add(entry[i])
                falta_pag += 1
                lugares.put(entry[i])
        else:
            # Caso os slots já estejam lotados, faz-se uma verificação
            # se caso a referência atual já está ou não dentro dos slots.
            if entry[i] not in pages:
                pg = lugares.queue[0]
                lugares.get()
                pages.remove(pg)
                pages.add(entry[i])
                lugares.put(entry[i])
                falta_pag += 1

        # Nesta parte do código, há a dinâmica de zerar o bit R a cada 4 referências à memória
        lista_auxiliar.extend(list(pages))  # A lista auxiliar vai add toda lista set de pages
        lista_auxiliar.sort()               # e em seguida ordena
        for j in list(pages):
            if lista_auxiliar.count(j) == 5:                # Quando um processo aparece 5 vezes nessa lista
                lista_auxiliar = list(set(lista_auxiliar))  
                val = lugares.queue[0]                      
                lugares.get()                           
                lugares.put(val)                            # ele é resetado e volta para o final da fila
    print("SC %d" % (falta_pag))


# Função principal, recebe e transforma a entrada como descrito na questão
# primeiro elemento é a quantidade de slots na memória e todos os outros são referências
# a ela  
if __name__ == "__main__":
    # with open("file.txt", 'r') as entrada:
    #     l = entrada.read().split("\n")
        
    l = []
    while True:
        try:
            e = input()
            l.append(e)
        except EOFError:
            break

    lis = list(map(int, l))
    slots = lis[0]
    paginas = lis[1:]

    # print(paginas)
    secondChance(slots, paginas)                # Função do algoritmo de Segunda Chance
    algOtimo(slots, paginas)                # Função do Algoritmo Ótimo
    conjuntoTrabalho(slots, paginas)