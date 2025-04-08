import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.colors import ListedColormap


matriz = [
    [0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0]
]

def coloracao(matriz_adj):
    n = len(matriz_adj)
    cores = [-1] * n  

    graus = np.sum(matriz, axis=1)
    vertices_ordenados = sorted(range(n), key=lambda x: -graus[x])
    
    for v in vertices_ordenados:
        proibidas = set()
        for vizinho in range(n):
            if matriz_adj[v][vizinho] == 1 and cores[vizinho] != -1:
                proibidas.add(cores[vizinho])
        
        for cor in range(n):
            if cor not in proibidas:
                cores[v] = cor
                break
    
    return cores


cores = coloracao(matriz)

def verifica_coloracao(matriz_adj, cores):
    n = len(cores)
    for i in range(n):
        for j in range(n):
            if matriz_adj[i][j] == 1 and cores[i] == cores[j]:
                return False
    return True

# print(cores)
print(verifica_coloracao(matriz, cores))


G = nx.Graph()
n = len(matriz)
for i in range(n):
    G.add_node(i)

for i in range(n):
    for j in range(i, n):
        if matriz[i][j] == 1:
            G.add_edge(i, j)


paleta_cores = ['#FF6B6B', '#4ECDC4', '#FFD166', '#A1C181']


cor_nos = [paleta_cores[cores[i] % len(paleta_cores)] for i in range(n)]


plt.figure(figsize=(10, 8))
pos = nx.circular_layout(G) 
nx.draw_networkx_nodes(G, pos, node_color=cor_nos, node_size=1200, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_color='black', font_weight='bold', font_size=12)
legend_handles = []
cores_usadas = sorted(set(cores))
for c in cores_usadas:
    legenda = plt.Line2D([0], [0], marker='o', color='w',
                         markerfacecolor=paleta_cores[c % len(paleta_cores)],
                         markersize=10, label=f'Cor {c}')
    legend_handles.append(legenda)
plt.legend(handles=legend_handles, title='Cores atribuídas')
plt.title("Grafo com Coloração de Vértices", fontsize=16)
plt.axis('off')
plt.tight_layout()
plt.show()