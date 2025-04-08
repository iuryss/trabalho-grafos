import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.colors import ListedColormap

estados_lista = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
n = len(estados_lista)
estado_id = {}
for i in range(len(estados_lista)):
    estado_id[estados_lista[i]] = i

matriz_adjacencia = np.zeros((n, n), dtype=int)

conexoes = [
    ("AC", "AM"), ("AC", "RO"), ("AL", "SE"), ("AL", "BA"), ("AL", "PE"),
    ("AP", "PA"), ("AM", "RR"), ("AM", "PA"), ("AM", "MT"), ("AM", "RO"), ("BA", "SE"), ("BA", "AL"),
    ("BA", "PE"), ("BA", "PI"), ("BA", "TO"), ("BA", "GO"), ("BA", "MG"), ("CE", "RN"), ("CE", "PB"),
    ("CE", "PE"), ("CE", "PI"), ("DF", "GO"), ("DF", "MG"), ("ES", "BA"), ("ES", "MG"), ("ES", "RJ"),
    ("GO", "MT"), ("GO", "MS"), ("GO", "MG"), ("GO", "DF"), ("GO", "BA"), ("GO", "TO"), ("MA", "PA"),
    ("MA", "TO"), ("MA", "PI"), ("MT", "RO"), ("MT", "AM"), ("MT", "PA"), ("MT", "TO"), ("MT", "GO"),
    ("MT", "MS"), ("MS", "MT"), ("MS", "GO"), ("MS", "MG"), ("MS", "SP"), ("MS", "PR"), ("MG", "MS"),
    ("MG", "GO"), ("MG", "BA"), ("MG", "ES"), ("MG", "RJ"), ("MG", "SP"), ("MG", "DF"), ("PA", "AP"),
    ("PA", "RR"), ("PA", "AM"), ("PA", "MT"), ("PA", "TO"), ("PA", "MA"), ("PB", "RN"), ("PB", "CE"),
    ("PB", "PE"), ("PR", "MS"), ("PR", "SP"), ("PR", "SC"), ("PE", "AL"), ("PE", "PB"), ("PE", "CE"),
    ("PE", "PI"), ("PE", "BA"), ("PI", "MA"), ("PI", "TO"), ("PI", "BA"), ("PI", "PE"), ("PI", "CE"),
    ("RJ", "MG"), ("RJ", "ES"), ("RJ", "SP"), ("RN", "CE"), ("RN", "PB"), ("RO", "AC"), ("RO", "AM"),
    ("RO", "MT"), ("RR", "AM"), ("RR", "PA"), ("RS", "SC"), ("SC", "PR"), ("SC", "RS"), ("SE", "AL"),
    ("SE", "BA"), ("SP", "MS"), ("SP", "MG"), ("SP", "RJ"), ("SP", "PR"), ("TO", "PA"), ("TO", "MT"),
    ("TO", "GO"), ("TO", "BA"), ("TO", "PI"), ("TO", "MA")
]

for u, v in conexoes:
    i, j = estado_id[u], estado_id[v]
    matriz_adjacencia[i][j] = 1
    matriz_adjacencia[j][i] = 1


print(matriz_adjacencia)

def coloracao(matriz_adj):
    n = len(matriz_adj)
    cores = [-1] * n  

    graus = np.sum(matriz_adjacencia, axis=1)
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


cores = coloracao(matriz_adjacencia)

def verifica_coloracao(matriz_adj, cores):
    n = len(matriz_adj)
    for i in range(n):
        for j in range(n):
            if matriz_adj[i][j] == 1 and cores[i] == cores[j]:
                return False
    return True

# print(cores)
print(verifica_coloracao(matriz_adjacencia, cores))

G = nx.Graph()

for i, estado in enumerate(estados_lista):
    G.add_node(estado, color=cores[i])

for u, v in conexoes:
    G.add_edge(u, v)

paleta_cores = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFBE0B']

cor_nos = [paleta_cores[G.nodes[estado]['color'] % len(paleta_cores)] for estado in estados_lista]

plt.figure(figsize=(15, 12))
pos = nx.spring_layout(G, seed=42) 
nx.draw_networkx_nodes(G, pos, node_size=1500, node_color=cor_nos, edgecolors='black')
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
legend_handles = []
for i, cor in enumerate(paleta_cores):
    legend_handles.append(plt.Line2D([0], [0], marker='o', color='w', 
                                  markerfacecolor=cor, markersize=10, 
                                  label=f'Cor {i}'))
plt.legend(handles=legend_handles, title='Cores atribuídas')
plt.title("Grafo dos Estados Brasileiros Colorido", fontsize=15)
plt.axis('off')
plt.tight_layout()
plt.show()

