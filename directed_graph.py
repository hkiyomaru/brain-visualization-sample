#!/usr/bin/env python

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import argparse
from read_csv import Readcsv


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-query', action='store',dest='query',default='Hippocampal')
    parser.add_argument('-path', action='store', dest='path', default="datasets/nature13186-s2.csv")

    query = parser.parse_args().query
    path = parser.parse_args().path

    csv_reader = Readcsv(query, path)
    relation = csv_reader.get_conn()

    dg = nx.DiGraph()
    dg.add_edges_from(relation)
    
    # Specify the edges you want here
    # red_edges = [('CA3', 'CA3')]
    # edge_colours = ['black' if not edge in red_edges else 'red'
    #                 for edge in dg.edges()]
    # black_edges = [edge for edge in dg.edges() if edge not in red_edges]
    
    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(dg)
    nx.draw_networkx_nodes(dg, pos, cmap=plt.get_cmap('jet'))
    # nx.draw_networkx_edges(dg, pos, edgelist=red_edges, edge_color='r', arrows=True)
    # nx.draw_networkx_edges(dg, pos, edgelist=black_edges, arrows=True)
    nx.draw_networkx_edges(dg, pos, edgelist=relation, arrows=True)
    plt.show()
    
