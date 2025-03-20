import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

estados_lista = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
n = len(estados_lista)
estado_id = {}
for i in range(len(estados_lista)):
    estado_id[estados_lista[i]] = i

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

conexoes_unicas = {tuple(sorted(conexao)) for conexao in conexoes}
conexoes_unicas = list(conexoes_unicas)

arestas = len(conexoes_unicas)
matriz_incidencia = np.zeros((n, arestas), dtype=int)

for col, (u, v) in enumerate(conexoes_unicas):
    i, j = estado_id[u], estado_id[v]
    matriz_incidencia[i, col] = 1
    matriz_incidencia[j, col] = 1

graus = np.sum(matriz_incidencia, axis=1)

max_grau = np.max(graus)
min_grau = np.min(graus)

max_estados = []
for i in range(n):
    if graus[i] == max_grau:
        max_estados.append(estados_lista[i])

min_estados = []
for i in range(n):
    if graus[i] == min_grau:
        min_estados.append(estados_lista[i])

vizinhos_max = {}
vizinhos_min = {}

for estado in max_estados:
    vizinhos = []
    for i in range(n):
        if i != estado_id[estado]:  
            for col in range(arestas):
                if matriz_incidencia[estado_id[estado], col] == 1 and matriz_incidencia[i, col] == 1:
                    vizinhos.append(estados_lista[i])  
    vizinhos_max[estado] = vizinhos

for estado in min_estados:
    vizinhos = []
    for i in range(n):
        if i != estado_id[estado]:  
            for col in range(arestas):
                if matriz_incidencia[estado_id[estado], col] == 1 and matriz_incidencia[i, col] == 1:
                    vizinhos.append(estados_lista[i])
    vizinhos_min[estado] = vizinhos

grau_frequencia = Counter(graus)

print("Matriz de Incidência:")
for linha in matriz_incidencia:
    print(linha) 

print(f"Estados com maior grau ({max_grau}): {max_estados}")
for estado in max_estados:
    print(f"{estado}: {vizinhos_max[estado]}")

print(f"\nEstados com menor grau ({min_grau}): {min_estados}")
for estado in min_estados:
    print(f"{estado}: {vizinhos_min[estado]}")


plt.figure(figsize=(10, 5))
plt.bar(grau_frequencia.keys(), grau_frequencia.values(), color='skyblue', edgecolor='black')
plt.xlabel('Grau dos Vértices')
plt.ylabel('Frequência')
plt.title('Frequência de grau no grafo dos estados brasileiros')
plt.xticks(list(grau_frequencia.keys()))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
