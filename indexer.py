from searchengine import main
import os
import pickle
import sys

dataset_path = os.path.expanduser(sys.argv[1])

indexed_data_path = os.path.join(os.getcwd(), 'data')
docs_file = os.path.join(indexed_data_path, 'docs.pickle')
inverted_index_file = os.path.join(indexed_data_path, 'inverted_index.pickle')

docs, inverted_index = main.index(dataset_path)

with open(docs_file, mode='wb') as f:
    pickle.dump(docs, f)

with open(inverted_index_file, mode='wb') as f:
    pickle.dump(inverted_index, f)
