import csv
import numpy as np
from parse_partition import ParsePartition

link_data_path="datasets/nature13186-s4.csv"

class Readcsv(ParsePartition):
    def __init__(self, query, path, external):
        ParsePartition.__init__(self, query, path)
        self.external = external
        self.ldpath = link_data_path
        self.initialize()

    def initialize(self):
        reader = csv.reader(open(self.ldpath, 'r'))
        array = []
        self.header = next(reader)[1:]
        for row in reader:
            array.append(row[1:])
        array = np.array(array)
        self.conn_list = []
        self.targets = self.parse_partition()
        if self.external:
            self.set_external_conn(array)
            self.set_external_conn(array.T)
        else:
            self.set_internal_conn(array)
            self.set_internal_conn(array.T)

    def set_external_conn(self, array):
        rn = 0
        for row in array:
            if self.header[rn] not in self.targets:
                pass
            else:
                cn = 0
                for tf in row:
                    if tf != '0':
                        self.conn_list.append((self.header[rn], self.header[cn]))
                    cn += 1
            rn += 1

    def set_internal_conn(self, array):
        rn = 0
        for row in array:
            if self.header[rn] not in self.targets:
                pass
            else:
                cn = 0
                for tf in row:
                    if self.header[cn] in self.targets:
                        if tf != '0':
                            self.conn_list.append((self.header[rn], self.header[cn]))
                    cn += 1
            rn += 1


    def get_conn(self): #for networkx
        return list(set(self.conn_list))

if __name__ == '__main__':
    csv_reader = Readcsv("Hippocampal", "datasets/nature13186-s2.csv", False)
    print csv_reader.get_conn()

