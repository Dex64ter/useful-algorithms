# Função que indica qual requisição é a mais próxima da atual
# posição do braço do disco
def pegaMenorDistancia(dicio):
    for key, val in dicio.items():
        if val == min(dicio.values()):
            return key

# Função que auxilia no calculo da distância de cada requisição
# atualizando o dicionario dado com todas
# as distâncias sendo os valores das chaves
# e as chaves por sua vez são as requisições no disco
def attDistancias(posicao, reqs, dicio):
    for j in reqs:
        dicio[j] = abs(j - posicao)

# Algoritmo do Elevador
def evelador(inicio, reqs):             # OK
    quant_cil = 0                       # Inicio da contagem de cilindros
    maior_req = max(reqs)               # Seleciona o cilindro requisitado mais externa
    menor_req = min(reqs)               # e o cilindro com menor número de requisição
    quant_cil += maior_req - inicio     # Soma-se a diferença do início até o mais externo
    quant_cil += maior_req - menor_req  # Soma-se a diferença entre o mais externo e o de menor requisição

    print("ELEVADOR", quant_cil)        

# Algoritmo SSTF (Shortest Seek Time First)
def SSTF(Num, inicio, reqs):            # OK
    requests = reqs.copy()      # Utilizamos uma cópia 
    cil_reqs = {}               # Dicionario que guardaa as distancia
    quant_cil = 0               # contagem dos cilindros

    for i in requests:          # Exclue todas requisições que ultrapassam
        if i > Num:             # o limite do disco
            requests.remove(i)

    attDistancias(inicio, requests, cil_reqs)   # Atualiza o dicionario de distancias
    while requests:                         # loop while enquanto ainda existem requisições
        ex = pegaMenorDistancia(cil_reqs)   # na primeira verificação já adiciona a
        quant_cil += cil_reqs[ex]           # diferença do inicio com a próxima requisição de menor distância
        requests.remove(ex)                 # retira da pseudolista de requisições
        attDistancias(ex, requests, cil_reqs)   # Atualiza as distâncias
        del cil_reqs[ex]                        # Retira do dicionário já utilizado
        
    print("SSTF", quant_cil)

# Algoritmo FCFS (First Come, First Serve)
def FCFS(Num, inicio, reqs):            # OK
    quant_cil = 0       # incio da contagem

    for i in range(len(reqs)):
        if reqs[i] <= Num:          # Se a requisição for maior q o limite, não processa
            if quant_cil == 0:          # caso seja o início da contagem
                quant_cil += reqs[i] - inicio   # pega a diferença que vai ser a distância
                val = reqs[i]                   # guarda o valor da ultima requisição
            else:
                quant_cil += abs(reqs[i] - val) # pega a diferença que vai ser a distância
                val = reqs[i]               # guarda o valor da ultima requisição
    print("FCFS", quant_cil)


if __name__ == "__main__":
    l = []
    while True:
        try:
            e = input()
            l.append(e)
        except EOFError:
            break

    #processamento da entrada
    l = list(map(int, l))
    n_cilindros = l[0]
    pos_inicial = l[1]
    requisicoes = l[2:]
    
    # Chamadas das funções
    FCFS(n_cilindros, pos_inicial, requisicoes)
    SSTF(n_cilindros, pos_inicial, requisicoes)
    evelador(pos_inicial, requisicoes)