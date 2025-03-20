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

tabela_alpha = [0] * (n + 1)
tabela_beta = []

vizinhos = []  
for i in range(n): 
    vizinhos.append([])

for u, v in conexoes_unicas:
    i, j = estado_id[u], estado_id[v]
    vizinhos[i].append(j)
    vizinhos[j].append(i)

indice_atual = 0
for i in range(n):
    tabela_alpha[i] = indice_atual
    tabela_beta.extend(vizinhos[i])
    indice_atual += len(vizinhos[i])
tabela_alpha[n] = indice_atual

graus = [] 

for i in range(n):  
    quantidade_de_vizinhos = len(vizinhos[i])  
    graus.append(quantidade_de_vizinhos)

max_grau = max(graus)
min_grau = min(graus)

max_estados = []
for i in range(n):  
    if graus[i] == max_grau:  
        max_estados.append(estados_lista[i]) 
    
min_estados = []
for i in range(n):
    if graus[i] == min_grau:
        min_estados.append(estados_lista[i])


vizinhos_max = {}  

for estado in max_estados: 
    estado_index = estado_id[estado]  
    vizinhos_do_estado = [] 
    for j in vizinhos[estado_index]:  
        vizinhos_do_estado.append(estados_lista[j])  
    vizinhos_max[estado] = vizinhos_do_estado  

vizinhos_min = {}  

for estado in min_estados:  
    estado_index = estado_id[estado]  
    vizinhos_do_estado = []  
    for j in vizinhos[estado_index]:  
        vizinhos_do_estado.append(estados_lista[j])  
    vizinhos_min[estado] = vizinhos_do_estado  

grau_frequencia = Counter(graus)

print(f"Tabela Alpha: {tabela_alpha}")
print(f"Tabela Beta: {tabela_beta}")
print(f"\nEstados com maior grau ({max_grau}): {max_estados}")
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
