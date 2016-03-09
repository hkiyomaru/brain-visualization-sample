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
    parser.add_argument('-ldpath', action='store', dest='ldpath', default="datasets/nature13186-s4.csv")
    parser.add_argument('-external', action='store_true', dest='external')

    query = parser.parse_args().query
    path = parser.parse_args().path
    ldpath = parser.parse_args().ldpath
    external = parser.parse_args().external
    conn_status = "_external" if external else "_internal"
    write_path = write_dir + query + conn_status + ".csv"

    csv_reader = Readcsv(query, path, ldpath, external)
    conn_list = csv_reader.get_conn()
    extract_csv_for_gephi(conn_list, write_path)
