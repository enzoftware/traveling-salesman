from queue import PriorityQueue
import heapq as pq
from cargaradjencylist import cargar
from leerArchivo import distancia, leerDataSet
INF = float('inf')

vertices=leerDataSet('outfile.csv')
G = cargar(vertices) 

def ucs(G, s, e):
    print('Camino: ')
    n    = len(G)
    vis  = [False]*n
    gn   = [INF]*n
    path = [None]*n
    q    = []
    pq.heappush(q, (0, s))
    gn[s] = 0
    while len(q) > 0:
        g, u = pq.heappop(q)
        print(u)
        if not vis[u]:
            vis[u] = True
            if u == e:
                break
            
            for par in G[u]:
                v=par[0]
                w=par[1]
                if not vis[v]:
                    f = g + w
                    if f < gn[v]:
                        gn[v]   = f
                        path[v] = u
                        pq.heappush(q, (f, par[0]))
                        
    return path, gn

def inicio(G,inicio,final):
    #path,gasto = ucs(G,encontrarIndice(inicio),encontrarIndice(final))
    path,gasto = ucs(G,inicio,final)
    print(gasto)


def encontrarIndice(cod):
    for k,v in vertices.items():
        if v.codigo == cod:
            return v.index

def encontrarCodigo(indice):
    return vertices[indice].codigo

#inicio(G,'525701','552398')

inicio(G,3,12)