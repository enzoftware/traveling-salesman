class ClaseGrafo:
    def __init__(self):
        self.aristas = {}
        self.pesos = {}
    def vecinos(self, nodo):
        return self.aristas[nodo]
    def getPeso(self,nodoOrigen,nodoDestino):
        return self.pesos[(nodoOrigen + nodoDestino)]
    def __str__(self):
        s = ""
        for k in self.aristas:
            s += k + ": " + str(self.aristas[k])
        return s

    
class Nodo:
    def __init__(self,codigo,nombreCP,Y_X_coord):
        self.codigo = codigo
        self.nombreCP = nombreCP
        self.Y_X_Coord = Y_X_coord

    def __str__(self):
        return "%s Cod: %s  XYCoord: %f " % (self.nombreCP, self.codigo, self.Y_X_Coord)