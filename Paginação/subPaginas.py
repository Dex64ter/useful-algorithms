from queue import Queue

def pagesSub(slots, entry):
    pages = set()
    falha_pag = 0
    lista_auxiliar = []
    lugares = Queue()
    
    for i in range(len(entry)):
        if len(pages) < slots:
            if entry[i] not in pages:
                pages.add(entry[i])
                falha_pag += 1
                lugares.put(entry[i])
        else:
            if entry[i] not in pages:
                pg = lugares.queue[0]
                lugares.get()
                pages.remove(pg)
                pages.add(entry[i])
                lugares.put(entry[i])
                falha_pag += 1

        lista_auxiliar.extend(list(pages))
        lista_auxiliar.sort()
        for j in list(pages):
            if lista_auxiliar.count(j) == 5:
                lista_auxiliar = list(set(lista_auxiliar))
                lista_auxiliar.remove(j)
                val = lugares.queue[0]
                lugares.get()
                lugares.put(val)
        print(lista_auxiliar)
        # print(pages)
    return falha_pag

if __name__ == "__main__":
    with open("file.txt", 'r+') as entrada:
        e = list(map(int, entrada.read().split("\n")))
        slots = e[0]
        paginas = e[1:]
    print(paginas)
    result = pagesSub(slots, paginas)
    print(result)