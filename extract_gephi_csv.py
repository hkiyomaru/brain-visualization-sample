import argparse
import csv
from read_csv import Readcsv

write_dir = './gephi/'

def extract_csv_for_gephi(conn_list, write_path):
    writer = csv.writer(open(write_path, "ab"))
    for f in conn_list:
        appendList = list(f)
        writer.writerow(appendList)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-query', action='store',dest='query',default='Hippocampal')
    parser.add_argument('-path', action='store', dest='path', default="datasets/nature13186-s2.csv")

    query = parser.parse_args().query
    path = parser.parse_args().path
    write_path = write_dir + query + ".csv"

    csv_reader = Readcsv(query, path)
    conn_list = csv_reader.get_conn()
    extract_csv_for_gephi(conn_list, write_path)
