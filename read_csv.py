import csv
import numpy as np
from parse_partition import ParsePartition

class Readcsv(ParsePartition):
    def __init__(self, query, path, ldpath, external):
        ParsePartition.__init__(self, query, path)
        self.external = external
        self.ldpath = ldpath
        self.initialize()

    def initialize(self):
        reader = csv.reader(open(self.ldpath, 'r'))
        array = []
        self.col_header = next(reader)[1:]
        self.row_header = []
        for row in reader:
            self.row_header.append(row[0])
            array.append(row[1:])
        array = np.array(array)
        self.conn_list = []
        self.targets = self.parse_partition()
        if self.external:
            self.set_external_conn(array)
        else:
            self.set_internal_conn(array)

    def set_external_conn(self, array):
        rn = 0
        for row in array:
            if self.row_header[rn] not in self.targets:
                pass
            else:
                cn = 0
                for tf in row:
                    if float(tf) > 0.1:
                        self.conn_list.append((self.row_header[rn], self.col_header[cn]))
                    cn += 1
            rn += 1

    def set_internal_conn(self, array):
        rn = 0
        for row in array:
            if self.row_header[rn] not in self.targets:
                pass
            else:
                cn = 0
                for tf in row:
                    if self.col_header[cn] in self.targets:
                        if float(tf) > 0.1:
                            self.conn_list.append((self.row_header[rn], self.col_header[cn]))
                    cn += 1
            rn += 1


    def get_conn(self): #for networkx
        return list(set(self.conn_list))

if __name__ == '__main__':
    csv_reader = Readcsv("Hippocampal", "datasets/nature13186-s2.csv", "datasets/nature13186-s2.csv", False)
    print csv_reader.get_conn()

