import csv
from enum import Enum

class HeaderEnum(Enum):

    UBIGEO = 0
    DEP = 1
    PROV = 2
    DIST = 3
    CODCP = 4
    MNOMCP = 6
    CAPITAL = 7
    XGD = 15
    YGD = 16

included_cols = [0, 1, 2, 3, 4, 6, 15, 16]  # the cols of the wanted data


with open('cpoblados.csv', 'r') as fin, open('outfile3.csv', 'w') as fout:  # choose an input file to read and

    # a destination output file

    writer = csv.writer(fout, delimiter=',')  # divided by commas
    count = 0
    for row in csv.reader(fin, delimiter=','):

        if row[HeaderEnum.CAPITAL.value] == 3 or row[HeaderEnum.CAPITAL.value] == '3' :  # row in position 1

            # is DEPARTMENT row in position 2 is DISTRICT
            count = count + 1
            writer.writerow(list(row[i] for i in included_cols))
    print(count)

print(writer)