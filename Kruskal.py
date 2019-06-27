import heapq as hq
from time import time
from crear_grafo import cargar, leerDataSet

def find(s, a):
    if s[a] < 0:
        return a
    else:
        return find(s, s[a])
        


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

def naiveunion(s,a,b):
    pa = find(s, a) 
    pb = find(s, b)
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
def obtenerKruskal(numero):
    if numero == 1:
        centros,grafo = leerDataSet('outfile1.csv')
    if numero == 2:
        centros,grafo = leerDataSet('outfile2.csv')
    if numero == 3:
        centros,grafo = leerDataSet('outfile3.csv')
    
    listagrafo = cargar(centros,grafo)
    start_time = time()
    _, MST = kruskal(listagrafo)
    print(MST)
    elapsed_time = time() - start_time
    print("Elapsed time: %0.10f seconds." % elapsed_time)
    return MST, centros
#print(kruskal(G))
'''
start_time = time()
centros6,grafo6 = leerDataSet('outfile3.csv')
listagrafo = cargar(centros6,grafo6)

roots, MST = kruskal(listagrafo)
elapsed_time = time() - start_time
print("Elapsed time: %0.10f seconds." % elapsed_time)
'''
import matplotlib.pyplot as plt



def buscarCentroPoblado(orden,centros):
    for cep in centros.values():
        if cep[0] == orden:
            return cep[1]
def pintarAristas(aristas,color,centros):
    for arista in aristas:
        origen,destino,_ = arista
        o = buscarCentroPoblado(origen,centros)
        d = buscarCentroPoblado(destino, centros)
        x = [o.xgd,d.xgd]
        y = [o.ygd,d.ygd]
        plt.plot(x,y,color=color,marker="8",markerEdgeColor="black")


    
#Pintar grafo
#pintarAristas(listagrafo,"blue")
#Pintar arbol de expansion minima
#pintarAristas(MST,"blue")
#plt.show()