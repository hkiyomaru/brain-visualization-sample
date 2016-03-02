import csv
import numpy as np
from parse_partition import ParsePartition

filepath = "datasets/nature13186-s4.csv"
gephi_csv = './gephi.csv'

class Readcsv:
    def __init__(self, path=filepath):
        self.path = path
        self.initialize()

    def initialize(self):
        reader = csv.reader(open(self.path, 'r'))
        array = []
        self.header = next(reader)[1:]
        for row in reader:
            array.append(row[1:])
        self.array = np.array(array)
        self.conn_list = []
        target_reader = ParsePartition()
        targets = target_reader.parse_partition()
        self.set_conn(self.array, targets)
        self.set_conn(self.array.T, targets)
        
    def set_conn(self, array, targets):
        rn = 0
        for row in self.array:
            if self.header[rn] not in targets:
                pass
            else:
                cn = 0
                for tf in row:
                    if tf != '0':
                        self.conn_list.append((self.header[rn], self.header[cn]))
                    cn += 1
            rn += 1

    def get_conn(self): #for networkx
        return self.conn_list

    def extract_csv(self): #for gephi
        writer = csv.writer(open(gephi_csv, "ab"))
        for f in self.conn_list:
            appendList = list(f)
            writer.writerow(appendList)

if __name__ == '__main__':
    csv_reader = Readcsv()
    print csv_reader.get_conn()
    # csv_reader.extract_csv()
