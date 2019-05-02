from queue import PriorityQueue
import heapq as pq
from cargaradjencylist import cargar
from leerArchivo import distancia, leerDataSet
INF = float('inf')

vertices=leerDataSet('outfile.csv')
G = cargar(vertices) 

def ucs(G, s, e):
    n    = len(G)
    vis  = [False]*n
    gn   = [INF]*n
    path = [None]*n
    q    = []
    pq.heappush(q, (0, s))
    gn[s] = 0
    while len(q) > 0:
        g, u = pq.heappop(q)
        if not vis[u]:
            vis[u] = True
            if u == e:
                break
            for v, w in G[u]:
                if not vis[v]:
                    f = g + w
                    if f < gn[v]:
                        gn[v]   = f
                        path[v] = encontrarCodigo(u)
                        pq.heappush(q, (f, v))
                        
    return path, gn

def inicio(G,inicio,final):
    path,gasto = ucs(G,encontrarIndice(inicio),encontrarIndice(final))
    print(path)
    print(gasto)

def encontrarIndice(cod):
    for k,v in vertices.items():
        if v.codigo == cod:
            return v.index

def encontrarCodigo(indice):
    for k,v in vertices.items():
        if v.index == indice:
            return v.codigo

inicio(G,'525701','552398')