import argparse
from read_csv import Readcsv

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-query', action='store',dest='query',default='Hippocampal')
    parser.add_argument('-path', action='store', dest='path', default="datasets/nature13186-s2.csv")

    query = parser.parse_args().query
    path = parser.parse_args().path

    csv_reader = Readcsv(query, path)
    csv_reader.extract_csv()
