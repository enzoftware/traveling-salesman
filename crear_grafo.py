import csv
from ClaseGrafo import ClaseGrafo, Nodo


def distanciaHamilton(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)
def distanciaEuclides(x1,y1,x2,y2):
    return ((x2-x1)**2 +(y2-y1)**2)**0.5

def leerDataSet(nombreArchivo): #retorna un diccionario de los centros poblados
    centros = {}
    grafo = []
    try:
        archivo = open(nombreArchivo)
        e = 0
        for line in archivo:
                try:
                    #dictionary
                    registro = line.split(',')
                    ubigeo = registro[0]
                    dep = registro[1]
                    prov = registro[2]
                    dist = registro[3]
                    codcp = registro[4]
                    mnomcp = registro[5]
                    xcord = float(registro[6])
                    ycord = float(registro[7])
                    
                    #graphlist
                    grafo.append([])
                except:
                    continue
                centros[e] = (e,Nodo(codcp,mnomcp,xcord,ycord,dep,dist,prov,ubigeo,e))
                e +=1



    except FileNotFoundError:
        print("Archivo no encontrado.")

    finally:
        archivo.close()

    return centros, grafo


def cargar(vertices, grafo):
    e=0
    for key, value in vertices.items():
        for num, val in vertices.items():
            if num != key:
                grafo[e].append([num,distanciaEuclides(value[1].xgd,value[1].ygd,val[1].xgd,val[1].ygd)])
        e+=1
    return grafo

centros,grafo = leerDataSet('outfile1.csv')
listagrafo = cargar(centros,grafo)

def printg(g):
    for e in g:
        print(e)
        print('')

printg(listagrafo)