import csv
from enum import Enum


class HeaderEnum(Enum):
    UBIGEO = 0
    DEP = 1
    PROV = 2
    DIST = 3
    MNOMCP = 6


with open('cpoblados.csv', 'r') as fin, open('outfile.csv', 'w') as fout:  # choose an input file to read and
    # a destination output file
    writer = csv.writer(fout, delimiter=',')  # divided by commas
    for row in csv.reader(fin, delimiter=','):
        if row[HeaderEnum.DIST.value] == 'SAN JUAN DE LURIGANCHO':  # row in position 1 is DEPARTMENT /// row in position 2 is DISTRICT
            writer.writerow(row)
print(writer)
