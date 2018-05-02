from utils import dataset, helpers


def index(dataset_path):
    docs = dataset.load_20newsgroups(dataset_path)
    inverted_index = helpers.build_inverted_index(docs)

    return docs, inverted_index
