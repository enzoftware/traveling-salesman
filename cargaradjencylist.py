from leerArchivo import distancia, leerDataSet

def cargar(vertices):
    matriz=[]
    e=0
    for key, value in vertices:
        matriz.append([])
        for num, val in vertices:
            if num != key:
                matriz[e].append((num,distancia(value.xcord,value.ycord,val.xcord,val.ycord)))
        e+=1

vertices=leerDataSet('outfile.csv')
print(cargar(vertices))