import csv
from enum import Enum

class HeaderEnum(Enum):
    UBIGEO = 0
    DEP = 1
    PROV = 2
    DIST = 3
    CODCP = 4
    MNOMCP = 6
    XGD = 15
    YGD = 16

included_cols = [0, 1, 2, 3, 4, 6, 15, 16]  # the cols of the wanted data

headers = ['UBIGEO', 'DISTRITO', 'NOMBRE', 'COORD_X', 'COORD_Y']

district = input('Ingresa el distrito : ')

with open('cpoblados.csv', 'r') as fin, open('outfile.csv', 'w') as fout:  # choose an input file to read and
    # a destination output file
    writer = csv.writer(fout, delimiter=',')  # divided by commas
    writer.writerow(list( i for i in headers))

    for row in csv.reader(fin, delimiter=','):
        if row[HeaderEnum.DIST.value] == 'VILLA EL SALVADOR':  # row in position 1
            # is DEPARTMENT row in position 2 is DISTRICT
            writer.writerow(list(row[i] for i in included_cols))
print(writer)
