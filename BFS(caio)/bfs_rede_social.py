import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def puxar_rede(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        return json.load(arquivo)


def bfs(rede, inicio, destino):
    visitados = set()
    fila = deque([[inicio]])

    print(f"Iniciando busca de '{inicio}' ate '{destino}'\n")

    if inicio == destino:
        print("Usuario de origem eh o mesmo que o de destino.")
        return [inicio]

    while fila:
        caminho = fila.popleft()
        no = caminho[-1]

        print(f"Explorando caminho: {caminho}")
        print(f"Node atual: {no}")

        if no not in visitados:
            vizinhos = rede.get(no, [])
            print(f"Vizinhos de {no}: {vizinhos}")

            for vizinho in vizinhos:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                print(f"Adicionando novo caminho a fila: {novo_caminho}")
                fila.append(novo_caminho)

                if vizinho == destino:
                    print(f"\nDestino '{destino}' encontrado! Caminho: {novo_caminho}")
                    return novo_caminho

            visitados.add(no)
            print(f"Marcando {no} como visitado.\n")
        else:
            print(f"{no} ja foi visitado, ignorando.\n")

    print(f"\nNao ha caminho entre '{inicio}' e '{destino}'")
    return None


def visualizar_rede_social(rede, caminho=[]):
    G = nx.Graph()
    for usuario, amigos in rede.items():
        for amigo in amigos:
            G.add_edge(usuario, amigo)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=900, node_color='purple', font_size=10, font_weight='bold')
    
    if caminho:
        caminho_edges = [(caminho[i], caminho[i + 1]) for i in range(len(caminho) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=caminho_edges, edge_color='b', width=2)

    plt.show()

if __name__ == "__main__":
    rede = puxar_rede('BFS(caio)/rede_social.json')
    usuario_inicial = "Alice"
    usuario_destino = "Judy"

    caminho = bfs(rede, usuario_inicial, usuario_destino)

    if caminho:
        print(f"Caminho encontrado: {' -> '.join(caminho)}")
        print(f"Distancia: {len(caminho) - 1}")
    else:
        print(f"Caminho não encontrado entre {usuario_inicial} e {usuario_destino}.")

    visualizar_rede_social(rede, caminho)
