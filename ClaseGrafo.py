class ClaseGrafo:
    def __init__(self):
        self.vertices = {}
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
    def __init__(self,codigo,nombreCP,xgd,ygd,dep,dist,prov,ubigeo):
        self.codigo = codigo
        self.nombreCP = nombreCP
        self.xgd = xgd
        self.ygd =ygd
        self.ubigeo = ubigeo
        self.dep=dep
        self.prov = prov
        self.dist = dist

    def __str__(self):
        return "%s Cod: %s  cordX: %f cordY: %f" % (self.nombreCP, self.codigo, self.xgd, self.ygd)