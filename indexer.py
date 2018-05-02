from searchengine import indexer
import os
import pickle
import sys

dataset_path = os.path.expanduser(sys.argv[1])
docs, inverted_index = indexer.index(dataset_path)

indexed_data_path = os.path.join(os.getcwd(), 'data')
doc_files = os.path.join(indexed_data_path, 'docs.pickle')
inverted_index_file = os.path.join(indexed_data_path, 'inverted_index.pickle')

with open(doc_files, mode='wb') as f:
    pickle.dump(docs, f)

with open(inverted_index_file, mode='wb') as f:
    pickle.dump(inverted_index, f)
