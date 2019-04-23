import csv
from enum import Enum


class HeaderEnum(Enum):
    UBIGEO = 0
    DEP = 1
    PROV = 2
    DIST = 3
    MNOMCP = 6
    Y_X_COORD = 17


included_cols = [0, 1, 2, 3, 6, 17]  # the cols of the wanted data

with open('cpoblados.csv', 'r') as fin, open('outfile.csv', 'w') as fout:  # choose an input file to read and
    # a destination output file
    writer = csv.writer(fout, delimiter=',')  # divided by commas
    for row in csv.reader(fin, delimiter=','):
        if row[HeaderEnum.DIST.value] == 'VILLA EL SALVADOR':  # row in position 1
            # is DEPARTMENT row in position 2 is DISTRICT
            writer.writerow(list(row[i] for i in included_cols))
print(writer)
