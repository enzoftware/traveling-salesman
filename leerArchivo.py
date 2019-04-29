from os import system
import csv
from ClaseGrafo import ClaseGrafo, Nodo

def leerDataSet(nombreArchivo): #retorna un diccionario de los centros poblados
    vertices = {}
    archivo = open(nombreArchivo,'r')
    try:
        i = 0
        for line in csv.reader(archivo,delimiter=','):
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
                    mnomcp = registro[4]
                    xycoord = float(registro[5])
                except:
                    continue
                vertices[ubigeo] = (Nodo(ubigeo,mnomcp,xycoord))
    except FileNotFoundError:
        print("Archivo no encontrado.")
    finally:
        archivo.close()
    return vertices

def leeLA(nombreArchivo): #retorna un grafo
    grafo = ClaseGrafo()
    try:
        archivoAristas = open(nombreArchivo,'r')
        lineas = archivoAristas.readlines()
        n = len(lineas)
        c = 0
        
        for linea in lineas:
            linea = linea.replace('\n','')
            codigos = linea.split(',')
            nodo = codigos.pop(0)
            vecinos = codigos
            grafo.aristas[nodo] = vecinos
            p = (c/float(n)) * 100
            print("Leyendo aristas (" + str(round(p,2)) + "%)")
            c+=1
        
    except FileNotFoundError:
        print("Archivo no encontrado, el formato es: 'pesos.nombreArchivo' y 'nombreArchivo")
    finally:
        archivoAristas.close()
    return grafo

if __name__ == "__main__":
    vertices = leerDataSet("outfile.csv")
    for k in vertices:
        print(vertices[k])
    n = len(vertices)
    print("%s elementos." % str(n))