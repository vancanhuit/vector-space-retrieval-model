import pickle
import os
import sys
import math
from utils import textprocessing
from utils import helpers
from collections import Counter
''' Query '''

docs_file = os.path.join(os.getcwd(), 'data', 'docs.pickle')
inverted_index_file = os.path.join(
    os.getcwd(), 'data', 'inverted_index.pickle')

stopwords_file = os.path.join(os.getcwd(), 'resources', 'stopwords_en.txt')

# Deserialize data
with open(docs_file, 'rb') as f:
    docs = pickle.load(f)
with open(inverted_index_file, 'rb') as f:
    inverted_index = pickle.load(f)

stopwords = helpers.get_stopwords(stopwords_file)

dictionary = set(inverted_index.keys())

# Get query from command line
query = sys.argv[1]
# Preprocess query
query = textprocessing.preprocess_text(query, stopwords)
query = [word for word in query if word in dictionary]
query = Counter(query)

# Compute weights for words in query
for word, value in query.items():
    query[word] = inverted_index[word]['idf'] * (1 + math.log(value))

helpers.normalize(query)

scores = [[i, 0] for i in range(len(docs))]
for word, value in query.items():
    for doc in inverted_index[word]['postings_list']:
        index, weight = doc
        scores[index][1] += value * weight

scores.sort(key=lambda doc: doc[1], reverse=True)

print('----- Results ------ ')
for index, score in enumerate(scores):
    if score[1] == 0:
        break
    print('{}. {} - {}'.format(index + 1, docs[score[0]], score[1]))
