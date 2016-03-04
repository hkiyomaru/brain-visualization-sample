import csv
import numpy as np
from parse_partition import ParsePartition

link_data_path="datasets/nature13186-s4.csv"

class Readcsv(ParsePartition):
    def __init__(self, query, path):
        ParsePartition.__init__(self, query, path)
        self.ldpath = link_data_path
        self.initialize()

    def initialize(self):
        reader = csv.reader(open(self.ldpath, 'r'))
        array = []
        self.header = next(reader)[1:]
        for row in reader:
            array.append(row[1:])
        self.array = np.array(array)
        self.conn_list = []
        targets = self.parse_partition()
        self.set_conn(self.array, targets)
        self.set_conn(self.array.T, targets)
        
    def set_conn(self, array, targets):
        rn = 0
        for row in array:
            if self.header[rn] not in targets:
                pass
            else:
                cn = 0
                for tf in row:
                    if self.header[cn] in targets:
                        if tf != '0':
                            self.conn_list.append((self.header[rn], self.header[cn]))
                    cn += 1
            rn += 1

    def get_conn(self): #for networkx
        return self.conn_list

if __name__ == '__main__':
    csv_reader = Readcsv("Hippocampal", "datasets/nature13186-s2.csv")
    print csv_reader.get_conn()

