from utils import weighting
'''This module contains unit tests for functions in weighting module'''


class TestWeighting(object):
    def test_frequency(self):
        doc = ['a', 'a', 'b', 'b', 'a', 'c']
        frequency_a = weighting.frequency('a', doc)
        frequency_b = weighting.frequency('b', doc)
        frequency_c = weighting.frequency('c', doc)
        frequency_d = weighting.frequency('d', doc)

        assert frequency_a == 3
        assert frequency_b == 2
        assert frequency_c == 1
        assert frequency_d == 0

    def test_document_frequency(self):
        doc1 = ['a', 'a', 'b']
        doc2 = ['a', 'c', 'c']
        doc3 = ['a', 'b', 'b', 'a']
        corpus = [doc1, doc2, doc3]

        document_frequency_a = weighting.document_frequency('a', corpus)
        document_frequency_b = weighting.document_frequency('b', corpus)
        document_frequency_c = weighting.document_frequency('c', corpus)

        assert document_frequency_a == 3
        assert document_frequency_b == 2
        assert document_frequency_c == 1
