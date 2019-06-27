from read_file import distancia, leerDataSet

def cargar(vertices):
    matriz=[]
    e=0
    for key, value in vertices.items():
        matriz.append([])
        for num, val in vertices.items():
            # if num != key:
            matriz[e].append(distancia(value.xgd,value.ygd,val.xgd,val.ygd))
        e+=1
    return matriz