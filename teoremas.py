import numpy as np
import math

grafo1 = [
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0]
]

grafo2 = [
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0]
]

grafo3 = [
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0]
]

grafo4 = [
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0]
]

def tem_dirac(matriz):
    graus = np.sum(matriz, axis=1)
    if(len(graus) < 3):
        return False
    min_grau = math.ceil(len(graus)/2)

    for grau in graus:
        if(grau >= min_grau):
            continue
        else:
            return False
        
    return True


def tem_ore(matriz):
    graus = np.sum(matriz, axis=1)
    n = len(matriz)
    if(n < 3):
        return False
    somas = []

    for i in range(n):
        for j in range(n):
            if(i == j): 
                continue
            if(matriz[i][j] == 0):
                soma = graus[i]+graus[j]
                somas.append(soma)
                
    for soma in somas:
        if(soma >= n):
            continue
        else:
            return False
        
    return True


def tem_bondy_chvatal(matriz):
    n = len(matriz)
    if(n < 3):
        return False
    graus = np.sum(matriz, axis=1)
    copia_matriz =np.array(matriz)

    for i in range(n):
        for j in range(n):
            if(i == j): 
                continue
            if(matriz[i][j] == 0):
                soma = graus[i]+graus[j]

                if(soma >= n):
                    copia_matriz[i][j] = 1
                    copia_matriz[j][i] = 1
                    graus[i] += 1
                    graus[j] += 1 
                    for k in range(i):
                        for m in range(j):
                            if(k == m): 
                                continue
                            if(copia_matriz[k][m] == 0):
                                sub_soma = graus[k]+graus[m]

                                if(sub_soma >= n):
                                    copia_matriz[k][m] = 1
                                    copia_matriz[m][k] = 1


    for i in range(n):
        for j in range(n):
            if(i == j): 
                continue
            if(copia_matriz[i][j] == 0):
                return False
    
    return True


def verificar_teoremas(matriz):
    if(tem_dirac(matriz)):
        print("O grafo é hamiltoniano de acordo com dirac")
    else:
        print("O grafo não é hamiltoniano de acordo com dirac")
    
    if(tem_ore(matriz)):
        print("O grafo é hamiltoniano de acordo com ore")
    else:
        print("O grafo não é hamiltoniano de acordo com ore")

    if(tem_bondy_chvatal(matriz)):
        print("O grafo é hamiltoniano de acordo com Bondy & Chvátal")
    else:
        print("O grafo não é hamiltoniano de acordo com Bondy & Chvátal")


print("Grafo 1: ")
verificar_teoremas(grafo1)
print()
print("Grafo 2: ")
verificar_teoremas(grafo2)
print()
print("Grafo 3: ")
verificar_teoremas(grafo3)
print()
print("Grafo 4: ")
verificar_teoremas(grafo4)
print()

