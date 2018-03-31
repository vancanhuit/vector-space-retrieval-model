import os
from collections import defaultdict
import math
''' Helper functions '''


def get_stopwords(stopwords_file):
    with open(stopwords_file, mode='r') as f:
        stopwords = set(f.read().split())
    return stopwords


def get_docs(dataset_path):
    docs = []
    for doc_file in os.listdir(dataset_path):
        docs.append(os.path.join(dataset_path, doc_file))
    return docs


def compute_idf(corpus):
    num_docs = len(corpus)
    idf = defaultdict(lambda: 0)
    for doc in corpus:
        for word in doc.keys():
            idf[word] += 1

    for word, value in idf.items():
        idf[word] = math.log(num_docs / value)
    return idf


def compute_weights(idf, doc):
    for word, value in doc.items():
        doc[word] = idf[word] * (1 + math.log(value))


def normalize(doc):
    denominator = math.sqrt(sum([e ** 2 for e in doc.values()]))
    for word, value in doc.items():
        doc[word] = value / denominator


def build_inverted_index(idf, corpus):
    inverted_index = {}
    for word, value in idf.items():
        inverted_index[word] = {}
        inverted_index[word]['idf'] = value
        inverted_index[word]['postings_list'] = []

    for index, doc in enumerate(corpus):
        for word, value in doc.items():
            inverted_index[word]['postings_list'].append([index, value])

    return inverted_index
