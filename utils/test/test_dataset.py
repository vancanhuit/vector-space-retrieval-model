import os
from utils import dataset


class TestDataset(object):
    def test_load_20newsgroups(self):
        dataset_path = os.path.expanduser('~/Documents/MIR/20_newsgroups')
        assert os.path.exists(dataset_path)
        assert os.path.isdir(dataset_path)
        docs = dataset.load_20newsgroups(dataset_path)
        assert len(docs) == 19997
