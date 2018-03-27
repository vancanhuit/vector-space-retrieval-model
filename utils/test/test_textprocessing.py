from utils import textprocessing
'''This module contains unit tests for text processing module'''


class TestTextProcessing(object):
    def test_remove_nonwords(self):
        text = "a'b c 123 * + - /"
        processed_text = textprocessing.remove_nonwords(text)

        assert type(processed_text) is str
        assert len(processed_text) == 5
        assert processed_text[0] == 'a'
        assert processed_text[1] == "'"
        assert processed_text[2] == 'b'
        assert processed_text[3] == ' '
        assert processed_text[4] == 'c'

    def test_remove_stopwords(self):
        text = 'there is some stopwords in the sentence'
        stopwords = {'is', 'in', 'the', 'some'}
        words = textprocessing.remove_stopwords(text, stopwords)

        assert type(words) is list
        assert len(words) == 3
        assert words[0] == 'there'
        assert words[1] == 'stopwords'
        assert words[2] == 'sentence'

    def test_stem_words(self):
        words = ['computer', 'computing']
        stemmed_words = textprocessing.stem_words(words)

        assert type(stemmed_words) is list
        assert stemmed_words[0] == stemmed_words[1]

    def test_preprocess_text(self):
        text = 'the computer is a computing device'
        stopwords = {'the', 'is', 'a'}
        words = textprocessing.preprocess_text(text, stopwords)

        assert type(words) is list
        assert len(words) == 3
        assert words[0] == 'comput'
        assert words[0] == words[1]
