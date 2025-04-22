import json

def dfs_com_pilha(grafo, inicio):
    visitados = set()  
    pilha = [inicio] 

    while pilha:
        vertice = pilha.pop() 
        if vertice not in visitados:
            visitados.add(vertice)  

            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    pilha.append(vizinho)

    return visitados


def rede_esta_conectada(grafo, roteador_central):
    visitados = dfs_com_pilha(grafo, roteador_central)
    return len(visitados) == len(grafo)

def puxar_rede(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        return json.load(arquivo)
    
rede_conectada = puxar_rede('DFS_Pilha(Iury)/rede_conectada.json')
rede_desconectada = puxar_rede('DFS_Pilha(Iury)/rede_desconectada.json')

print("Rede conectada: ", rede_esta_conectada(rede_conectada, 'R1'))
print("Rede desconectada: ", rede_esta_conectada(rede_desconectada, 'R1'))