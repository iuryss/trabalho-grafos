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
    if origem not in grafo or destino not in grafo:
        return None, float("inf"), {}

    fila = [(0, origem)]
    visitados = set()
    distancias = {origem: 0}
    pais = {origem: None}

    while fila:
        custo, atual = heapq.heappop(fila)

        if atual in visitados:
            continue

        visitados.add(atual)

        if atual == destino:
            break

        for vizinho, peso in grafo.get(atual, []):
            novo_custo = custo + peso
            if vizinho not in distancias or novo_custo < distancias[vizinho]:
                distancias[vizinho] = novo_custo
                pais[vizinho] = atual
                heapq.heappush(fila, (novo_custo, vizinho))

    caminho = []
    atual = destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = pais.get(atual)

    if caminho and caminho[0] == origem:
        return caminho, distancias[destino], pais
    else:
        return None, float("inf"), {}

def mostrar_resultado(origem, destino):
    caminho, custo_total, pais = dijkstra(grafo, origem, destino)

    if caminho:
        print(f"Caminho mais curto de {origem} até {destino}: {' -> '.join(caminho)}")
        print(f"Custo total (em minutos): {custo_total}")
        print("\nPais de cada nó no caminho:")
        for no in caminho[1:]:  # ignorar origem pois não tem pai
            print(f"{no} veio de {pais[no]}")
    else:
        print(f"Não foi possível encontrar um caminho de {origem} até {destino}.")

# Exemplo de uso
mostrar_resultado("Centro", "Messejana")
