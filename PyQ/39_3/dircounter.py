import os


def count_files(dirpath):
    return len(os.listdir(dirpath))
