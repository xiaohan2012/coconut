# coding: utf-8

import numpy as np
import pandas as pd
import pickle as pkl
import networkx as nx
from collections import defaultdict
from itertools import combinations
from scipy.sparse import csr_matrix
from tqdm import tqdm


graph_output_path = 'data/datascience.graph.pkl'
meta_info_output_path = 'data/datascience.meta.pkl'

df = pd.read_csv('data/datascience_labels.csv', sep=',', header=None)  # the co-occurence data

rows = [r.split(',') for r in df[1]]


all_labels = set([l for r in rows for l in r])

label2id = {l: i for i, l in enumerate(all_labels)}

N = len(label2id)

graph = defaultdict(lambda: defaultdict(int))

for r in tqdm(rows):
    for u, v in combinations(r, 2):
        u, v = sorted([u, v])
        graph[label2id[u]][label2id[v]] += 1

indices_and_data = [(u, v, graph[u][v]) for u in graph for v in graph[u]]

row_ind, col_ind, data = zip(*indices_and_data)

data = np.log(np.array(data) + 1)

m = csr_matrix((data, (row_ind, col_ind)), shape=(N, N))

g = nx.from_scipy_sparse_matrix(m)

nx.write_gpickle(g, graph_output_path)
pkl.dump(label2id, open(meta_info_output_path, 'wb'))


print("size(s) of connected component(s)", list(map(len, nx.connected_components(g))))

