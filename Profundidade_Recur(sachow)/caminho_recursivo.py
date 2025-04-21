import json

def carregar_grafo_json(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)

def buscar_caminho(grafo, origem, destino, caminho=None):
    if caminho is None:
        caminho = []

    caminho = caminho + [origem]

    if origem == destino:
        return caminho

    vizinhos = grafo.get(origem, [])

    return buscar_vizinhos_recursivamente(grafo, vizinhos, destino, caminho, 0)

def buscar_vizinhos_recursivamente(grafo, vizinhos, destino, caminho, indice):
    if indice >= len(vizinhos):
        return None

    vizinho = vizinhos[indice]

    if vizinho not in caminho:
        novo_caminho = buscar_caminho(grafo, vizinho, destino, caminho)
        if novo_caminho:
            return novo_caminho

    return buscar_vizinhos_recursivamente(grafo, vizinhos, destino, caminho, indice + 1)

def imprimir_caminho_recursivo(caminho, indice=0):
    if indice >= len(caminho):
        return
    print(caminho[indice], end=" -> " if indice < len(caminho) - 1 else "\n")
    imprimir_caminho_recursivo(caminho, indice + 1)

def main():
    grafo = carregar_grafo_json('cidades.json')

    origem = input("Digite a cidade de origem: ").strip()
    destino = input("Digite a cidade de destino: ").strip()

    if origem not in grafo or destino not in grafo:
        print("Cidade inválida.")
        return

    caminho = buscar_caminho(grafo, origem, destino)

    if caminho:
        print("Caminho encontrado:")
        imprimir_caminho_recursivo(caminho)
    else:
        print(f"Nenhum caminho encontrado entre {origem} e {destino}.")

if __name__ == "__main__":
    main()
