from utils import dataset, helpers, textprocessing
from nltk.corpus import stopwords
from collections import Counter
import math


def index(dataset_path):
    docs = dataset.load_20newsgroups(dataset_path)
    inverted_index = helpers.build_inverted_index(docs)

    return docs, inverted_index


def search(query, docs, inverted_index):
    dictionary = set(inverted_index.keys())
    stop_words = set(stopwords.words('english'))
    query = textprocessing.preprocess_text(query, stop_words)
    query = [word for word in query if word in dictionary]
    processed_query = Counter(query)

    for word, value in processed_query.items():
        processed_query[word] = inverted_index[word]['idf'] * (
            1 + math.log(value))

    helpers.normalize(processed_query)
    scores = [[i, 0] for i in range(len(docs))]
    for word, value in processed_query.items():
        for doc in inverted_index[word]['postings_list']:
            index, weight = doc
            scores[index][1] += value * weight

    scores.sort(key=lambda doc: doc[1], reverse=True)
    for index, score in enumerate(scores):
        yield index, score
