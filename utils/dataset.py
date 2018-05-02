import os


def load_20newsgroups(dataset_path):
    docs = []
    for dirname in os.listdir(dataset_path):
        dir_path = os.path.join(dataset_path, dirname)
        for filname in os.listdir(dir_path):
            file_path = os.path.join(dir_path, filname)
            docs.append(file_path)
    return docs
