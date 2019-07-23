from kruskal import *

with open('aeropuertos1.in') as f:
    line = f.readline().strip()
    N, M, A = [int(x) for x in line.split(' ')]
    G = [[] for _ in range(N)]
    for _ in range(M):
        line = f.readline().strip()
        u, v, c = [int(x) for x in line.split(' ')]
        u -= 1
        v -= 1
        G[u].append((v, c))
        #G[v].append((u, c))
    print(G)

r, t = kruskal(G)

print(r, t)
s = 0
for _, _, C in t:
    s += C
for x in r:
    if x < 0:
        s += A

print(s)


