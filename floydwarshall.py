import math

class FloydWarshall:
    def __init__(self, W):
        self.n = len(W)
        self.W = W
        self.d = []
        for i in range(self.n):
            linha = []
            for j in range(self.n):
                linha.append(W[i][j])
            self.d.append(linha)        
        self.p = []
        for i in range(self.n):
            linha = []
            for j in range(self.n):
                if i == j or W[i][j] == math.inf:
                    linha.append(None)
                else:
                    linha.append(i)
            self.p.append(linha)

    def rodar_algoritmo(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.d[i][k] + self.d[k][j] < self.d[i][j]:
                        self.d[i][j] = self.d[i][k] + self.d[k][j]
                        self.p[i][j] = self.p[k][j]

    def reconstruir_caminho(self, i, j):
        if self.d[i][j] == math.inf:
            return None
        caminho = [j]
        while i != j:
            j = self.p[i][j]
            if j is None:
                return None
            caminho.insert(0, j)
        return caminho

    def mostrar_matriz(self, M):
        for linha in M:
            nova_linha = []
            for x in linha:
                if x == math.inf:
                    nova_linha.append('∞')
                else:
                    nova_linha.append(x)
            print(nova_linha)

        print()

    def mostrar_resultados(self):
        print("Matriz de distâncias mínimas (dn):")
        self.mostrar_matriz(self.d)

        print("Matriz de predecessores (pn):")
        self.mostrar_matriz(self.p)

        print("Caminhos mínimos entre todos os centros:")

        for i in range(self.n):
            for j in range(self.n):
                if i != j:
                    caminho = self.reconstruir_caminho(i, j)

                    if caminho is not None:
                        caminho_str = ""
                        for n in caminho:
                            centro_nome = "C" + str(n + 1)
                            if caminho_str == "":
                                caminho_str = centro_nome
                            else:
                                caminho_str = caminho_str + " → " + centro_nome

                        tempo_total = self.d[i][j]
                        print("C" + str(i + 1) + " → " + "C" + str(j + 1) + ": " + caminho_str + " (Tempo: " + str(tempo_total) + ")")
                    else:
                        print("C" + str(i + 1) + " → " + "C" + str(j + 1) + ": Sem caminho")


W = [
    [0, 2, math.inf, 8, math.inf],
    [math.inf, 0, 3, math.inf, math.inf],
    [math.inf, math.inf, 0, math.inf, 1],
    [math.inf, math.inf, 4, 0, math.inf],
    [math.inf, math.inf, math.inf, 5, 0]
]

fw = FloydWarshall(W)
fw.rodar_algoritmo()
fw.mostrar_resultados()
