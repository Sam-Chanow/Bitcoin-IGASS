###MODEL CLASS FOR the BPRI DATASET TRAINING###
###SAM CHANOW RYAN METZ###

import dataset


# This function will use BERT to vectorize a datset and return a new Dataset
def build_vector_data(raw_data):  # raw_data is a dataset object, and this will make a vectorized dataset for the model
    # Vector data writes the vectorized data to a file and returns a dataset object pointing to that file
    pass


# This function will clean a string of data
def clean(sentence):
    pass


class Model:
    def __init__(self):
        pass

    def train(self, train_d):
        pass

    def test(self, test_d):
        pass

    def evaluate(self, data_unlabeled):
        pass
