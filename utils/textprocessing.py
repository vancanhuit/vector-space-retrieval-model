import re
from nltk.stem.porter import PorterStemmer
''' Text processing '''


def remove_nonwords(text):
    non_words = re.compile(r"[^a-z']")
    processed_text = re.sub(non_words, ' ', text)
    return processed_text.strip()


def remove_stopwords(text, stopwords):
    words = [word for word in text.split() if word not in stopwords]
    return words


def stem_words(words):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    return stemmed_words


def preprocess_text(text, stopwords):
    processed_text = remove_nonwords(text.lower())
    words = remove_stopwords(processed_text, stopwords)
    stemmed_words = stem_words(words)
    return stemmed_words
