import os
import sys
import pickle
from searchengine import main

indexed_data_path = os.path.join(os.getcwd(), 'data')
docs_file = os.path.join(indexed_data_path, 'docs.pickle')
inverted_index_file = os.path.join(indexed_data_path, 'inverted_index.pickle')

with open(docs_file, mode='rb') as f:
    docs = pickle.load(f)
with open(inverted_index_file, mode='rb') as f:
    inverted_index = pickle.load(f)

query = sys.argv[1]
main.search(query, docs, inverted_index)
