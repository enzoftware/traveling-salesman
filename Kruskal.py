import heapq as hq
from time import time
from crear_grafo import cargar, leerDataSet

def find(s, a):
    if s[a] < 0:
        return a
    else:
        granpa = find(s, s[a])
        s[a] = granpa
        return granpa


def union(s, a, b):
    pa = find(s, a)
    pb = find(s, b)
    if pa == pb: return
    
    if s[pa] <= s[pb]:
        s[pa] += s[pb]
        s[pb] = pa
    elif s[pb] < s[pa]:
        s[pb] += s[pa]
        s[pa] = pb


def makeIL(G):
    il = []
    n = len(G)
    for u in range(n):
        for v, w in G[u]:
            il.append((w, u, v))
    return il


def kruskal(G):
    il = makeIL(G)
    q = []
    n = len(G)
    for edge in il:
        hq.heappush(q, edge)
    roots = [-1]*n
    T = []
    while len(q) > 0:
        w, u, v = hq.heappop(q)
        if find(roots, u) != find(roots, v):
            union(roots, u, v)
            T.append((u, v, w))
    return roots, T

'''
G = []
with open('grafito.in') as f:
    for line in f:
        u = len(G)
        G.append([])
        nums = [int(x) for x in line.split(' ')]
        for i in range(len(nums) // 2):
            G[u].append((nums[i * 2], nums[i * 2 + 1]))
'''
#print(kruskal(G))
start_time = time()
centros6,grafo6 = leerDataSet('outfile3.csv')
listagrafo = cargar(centros6,grafo6)



print(kruskal(listagrafo))
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)

import matplotlib.pyplot as plt

#Config mapa
plt.figure(figsize=(15,10))
plt.title("Mapa")
plt.xlabel("Coord X")
plt.ylabel("Coord Y")

#Pintando mapa
x = []
y = []
for cep in centros6.values():
    x.append(cep[1].xgd)
    y.append(cep[1].ygd)


plt.plot(x,y,'ro')
def buscarCentroPoblado(codigo):
    for cep in centros6:
        if cep.codigo == codigo:
            return cep
def pintarAristas(aristas,color):
    for arista in aristas:
        _,origen,destino = arista
        o = buscarCentroPoblado(origen)
        d = buscarCentroPoblado(destino)
        x = [o.coordX,d.coordX]
        y = [o.coordY,d.coordY]
        plt.plot(x,y,color=color,marker="8",markerEdgeColor="black")
    
#Pintar grafo
#pintarAristas(listagrafo,"blue")
#Pintar arbol de expansion minima
#pintarAristas(arbolExpMin,"white")
plt.show()