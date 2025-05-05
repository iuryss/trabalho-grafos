import heapq

grafo = {
    "Centro": [("Aldeota", 10), ("Benfica", 5)],
    "Aldeota": [("Centro", 10), ("Meireles", 6), ("Papicu", 8)],
    "Benfica": [("Centro", 5), ("Parangaba", 7)],
    "Meireles": [("Aldeota", 6), ("Papicu", 4)],
    "Papicu": [("Aldeota", 8), ("Meireles", 4), ("Messejana", 12)],
    "Parangaba": [("Benfica", 7), ("Messejana", 10)],
    "Messejana": [("Papicu", 12), ("Parangaba", 10)]
}

def dijkstra(grafo, origem, destino):
    fila = [(0, origem, [])]  # (custo atual, vértice atual, caminho até aqui)
    visitados = set()

    while fila:
        custo, atual, caminho = heapq.heappop(fila)

        if atual in visitados:
            continue

        caminho = caminho + [atual]
        visitados.add(atual)

        if atual == destino:
            return caminho, custo

        for vizinho, peso in grafo.get(atual, []):
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + peso, vizinho, caminho))

    return None, float("inf")  # se não encontrar caminho

origem = "Centro"
destino = "Messejana"

caminho, custo_total = dijkstra(grafo, origem, destino)

print("Caminho mais curto:", " -> ".join(caminho))
print("Custo total (em minutos):", custo_total)
