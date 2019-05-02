from os import system
import csv
from ClaseGrafo import ClaseGrafo, Nodo


def distancia(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def leerDataSet(nombreArchivo): #retorna un diccionario de los centros poblados
    vertices = {}
    try:
        archivo = open(nombreArchivo)
        i = 0
        e = 0
        for line in archivo:
            if i == 0:
                i += 1
                continue
            else:
                try:
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
                vertices[e] = (Nodo(codcp,mnomcp,xcord,ycord,dep,dist,prov,ubigeo,e))
                e +=1

    except FileNotFoundError:
        print("Archivo no encontrado.")
    finally:
        archivo.close()
    return vertices
