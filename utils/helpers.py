import os
from collections import defaultdict
from nltk.corpus import stopwords
from utils import textprocessing
from collections import Counter
import math
''' Helper functions '''


def create_corpus(docs):
    stop_words = set(stopwords.words('english'))
    for doc in docs:
        with open(doc, mode='r', encoding='iso-8859-1') as f:
            text = f.read()
            words = textprocessing.preprocess_text(text, stop_words)
            bag_of_words = Counter(words)
            yield bag_of_words


def compute_idf(docs):
    num_docs = len(docs)
    corpus = create_corpus(docs)

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


def build_inverted_index(docs):
    idf = compute_idf(docs)

    inverted_index = {}
    for word, value in idf.items():
        inverted_index[word] = {}
        inverted_index[word]['idf'] = value
        inverted_index[word]['postings_list'] = []

    corpus = create_corpus(docs)
    for index, doc in enumerate(corpus):
        compute_weights(idf, doc)
        normalize(doc)
        for word, value in doc.items():
            inverted_index[word]['postings_list'].append([index, value])

    return inverted_index
