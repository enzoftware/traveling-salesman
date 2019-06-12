import csv
from ClaseGrafo import ClaseGrafo, Nodo


def distancia(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)



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
                except:
                    continue
                centros[e] = (e,Nodo(codcp,mnomcp,xcord,ycord,dep,dist,prov,ubigeo,e))
                e +=1



    except FileNotFoundError:
        print("Archivo no encontrado.")

    finally:
        archivo.close()

    return centros, grafo


def cargar(vertices):
    matriz=[]
    e=0
    for key, value in vertices.items():
        matriz.append([])
        for num, val in vertices.items():
            if num != key:
                matriz[e].append([num,distancia(value.xgd,value.ygd,val.xgd,val.ygd)])
        e+=1
    return matriz