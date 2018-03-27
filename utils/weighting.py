'''This module contains function for computing
term frequency, inverse document frequency and weight'''


def frequency(term, doc):
    return doc.count(term)


def document_frequency(term, corpus):
    df = 0
    for doc in corpus:
        if frequency(term, doc) != 0:
            df += 1
    return df


def term_frequency(term, doc):
    pass


def inverse_document_frequency(term, corpus):
    pass


def tf_idf(tf, idf):
    return tf * idf
