import numpy as np
import seaborn as sns
import shapefile as shp
import matplotlib.pyplot as plt
from Kruskal import pintarAristas,obtenerKruskal

sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))

shp_path = "perumap1\per_admbnda_adm1_2018.shp"
sf = shp.Reader(shp_path)

def plot_map(sf, x_lim = None, y_lim = None, figsize = (11,9)):
    '''
    Plot map with lim coordinates
    '''
    plt.figure(figsize = figsize)
    id=0
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, 'k')
        
        if (x_lim == None) & (y_lim == None):
            x0 = np.mean(x)
            y0 = np.mean(y)
            plt.text(x0, y0, id, fontsize=10)
        id = id+1
    
    if (x_lim != None) & (y_lim != None):     
        plt.xlim(x_lim)
        plt.ylim(y_lim)

plot_map(sf)

pintarAristas(obtenerKruskal(3),"blue")

plt.show()